"""Abre um .zip remoto por pedidos HTTP Range (via curl, com os certificados do sistema), sem gravar nada em disco.
Uso: z = open_remote_zip(url); z.namelist(); z.open(nome) devolve um fluxo descompactado."""
import io
import subprocess
import zipfile


def _curl(args, timeout=400):
    for tentativa in range(5):
        r = subprocess.run(["curl", "-sL", "--fail", "--max-time", str(timeout), *args], capture_output=True)
        if r.returncode == 0:
            return r.stdout
    raise RuntimeError(f"curl falhou: {args[-1]} ({r.returncode})")


class HTTPFile(io.RawIOBase):
    def __init__(self, url):
        self.url = url
        cab = _curl(["-I", url], 60).decode("latin1")
        self.size = int([l.split(":")[1] for l in cab.splitlines() if l.lower().startswith("content-length")][-1])
        self.pos = 0

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, off, whence=0):
        self.pos = {0: off, 1: self.pos + off, 2: self.size + off}[whence]
        return self.pos

    def readinto(self, b):
        n = len(b)
        if n == 0 or self.pos >= self.size:
            return 0
        end = min(self.pos + n, self.size) - 1
        data = _curl(["-r", f"{self.pos}-{end}", self.url])
        b[: len(data)] = data
        self.pos += len(data)
        return len(data)


def open_remote_zip(url, buffer_mb=8):
    return zipfile.ZipFile(io.BufferedReader(HTTPFile(url), buffer_size=buffer_mb * 1024 * 1024))


class Deflate64Stream(io.RawIOBase):
    """Lê uma entrada de zip compactada com Deflate64 (método 9), que o módulo zipfile não abre.
    Precisa do pacote inflate64 (PyPI)."""

    def __init__(self, z, info, bloco=1 << 20):
        import struct
        import inflate64
        self._fp = z.fp
        self._fp.seek(info.header_offset)
        cab = self._fp.read(30)
        n, m = struct.unpack("<HH", cab[26:30])
        self._pos = info.header_offset + 30 + n + m
        self._restante = info.compress_size
        self._bloco = bloco
        self._inf = inflate64.Inflater()
        self._buf = b""

    def readable(self):
        return True

    def readinto(self, b):
        while not self._buf and self._restante > 0:
            self._fp.seek(self._pos)
            dados = self._fp.read(min(self._bloco, self._restante))
            self._pos += len(dados)
            self._restante -= len(dados)
            self._buf = self._inf.inflate(dados)
        if not self._buf:
            return 0
        n = min(len(b), len(self._buf))
        b[:n] = self._buf[:n]
        self._buf = self._buf[n:]
        return n


def abrir_entrada(z, info):
    """z.open(info) para qualquer método, inclusive Deflate64."""
    if info.compress_type == 9:
        return io.BufferedReader(Deflate64Stream(z, info), buffer_size=8 << 20)
    return z.open(info)
