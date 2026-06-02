#!/usr/bin/env python3
"""
converte_posts.py
Converte .md do Medium (cabecalho em prosa) para o formato do blog datavizbr.

- Frontmatter YAML alinhado com content.config.ts
- Nome do arquivo = slug gerado do titulo
- Autores convertidos para IDs (slugs)

Uso:
    python converte_posts.py ./entrada ./saida

Coloque na raiz do projeto. Os arquivos convertidos vao para ./saida,
prontos para mover para src/content/posts/
"""

import sys, re, unicodedata, datetime
from pathlib import Path

MESES = {
    "jan":1,"feb":2,"fev":2,"mar":3,"apr":4,"abr":4,"may":5,"mai":5,
    "jun":6,"jul":7,"aug":8,"ago":8,"sep":9,"set":9,"oct":10,"out":10,
    "nov":11,"dec":12,"dez":12,
}

# Mapa nome → ID (slug do arquivo em src/content/autores/)
AUTORES = {
    "rodrigo medeiros":        "rodrigo-medeiros",
    "daniel souza":            "daniel-souza",
    "adolfo guimaraes":        "adolfo-guimaraes",
    "carol cavaleiro":         "carol-cavaleiro",
    "carolina leslie":         "carolina-leslie",
    "deborah mesquita":        "deborah-mesquita",
    "déborah mesquita":        "deborah-mesquita",
    "elijah meeks":            "elijah-meeks",
    "eliza fernandes":         "eliza-fernandes",
    "eliza fagundes":          "eliza-fernandes",
    "elmo neto":               "elmo-neto",
    "fernando barbalho":       "fernando-barbalho",
    "fernando hannaka":        "fernando-hannaka",
    "gabriel vaz de melo":     "gabriel-vaz-de-melo",
    "gabriela momberg":        "gabriela-momberg",
    "gabriella s. de macedo":  "gabriella-s-de-macedo",
    "gabriella sales de macedo": "gabriella-s-de-macedo",
    "glaudemias g. junior":    "glaudemias-g-junior",
    "igor falconieri":         "igor-falconieri",
    "isabela noronha":         "isabela-noronha",
    "juliana freitas":         "juliana-freitas",
    "ligia galvao":            "ligia-galvao",
    "lígia galvão":            "ligia-galvao",
    "lucas gomes":             "lucas-gomes",
    "marck al":                "marck-ai",
    "marck ai":                "marck-ai",
    "mauro pinheiro":          "mauro-pinheiro",
    "olga lopes":              "olga-lopes",
    "ricardo brasileiro":      "ricardo-brasileiro",
    "ricardo brazileiro":      "ricardo-brasileiro",
    "ricardo cunha lima":      "ricardo-cunha-lima",
    "rodolfo almeida":         "rodolfo-almeida",
    "rodrigo menegat":         "rodrigo-menegat",
    "salome esteves":          "salome-esteves",
    "salomé esteves":          "salome-esteves",
    "stephanie evergreen":     "stephanie-evergreen",
    "tatyana mendes":          "tatyana-mendes",
    "vinicius c. barqueiro":   "vinicius-c-barqueiro",
    "vinícius c. barqueiro":   "vinicius-c-barqueiro",
    "william r. cordeiro":     "william-r-cordeiro",
}

# Tenta classificar a secao pelo conteudo
def classificar_secao(titulo, corpo):
    texto = (titulo + " " + corpo[:600]).lower()
    if any(w in texto for w in ["tutorial", "passo a passo", "como fazer", "como criar",
                                 "qgis", "ferramenta", "guia", "pratica", "tecnica"]):
        return "praticas"
    if any(w in texto for w in ["entrevista", "conversa", "bastidor", "como fiz",
                                 "processo", "por tras", "relato"]):
        return "bastidores"
    if any(w in texto for w in ["panorama", "survey", "mapa da cena", "estado da arte",
                                 "overview", "quem e quem", "lista"]):
        return "panorama"
    return "ensaios"

def slugify(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return re.sub(r"-{2,}", "-", t)[:80]

def parse_data(s):
    s = s.strip()
    m = re.match(r"([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})", s)
    if m:
        mes = MESES.get(m.group(1)[:3].lower())
        if mes:
            return datetime.date(int(m.group(3)), mes, int(m.group(2)))
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None

def resolver_autor(raw):
    """Retorna (ids_encontrados, nomes_nao_encontrados)"""
    base = re.sub(r"\(.*?\)", "", raw).strip()
    partes = re.split(r"\s*(?:,| e )\s*", base)
    ids, faltando = [], []
    for p in partes:
        if not p.strip():
            continue
        k = p.strip().lower()
        if k in AUTORES:
            ids.append(AUTORES[k])
        else:
            faltando.append(p.strip())
    return ids, faltando

def processar(texto):
    linhas = texto.splitlines()
    titulo = autor = data = url = None
    ini = 0
    for i, ln in enumerate(linhas):
        if ln.startswith("# "):
            titulo = ln[2:].strip()
            ini = i + 1
            break
    for i in range(ini, min(ini + 12, len(linhas))):
        ln = linhas[i].strip()
        if ln.startswith("**Autor:**"):
            autor = ln.replace("**Autor:**", "").strip()
        elif ln.startswith("**Data:**"):
            data = ln.replace("**Data:**", "").strip()
        elif ln.startswith("**URL:**"):
            url = ln.replace("**URL:**", "").strip()
        elif ln == "---":
            ini = i + 1
            break
    corpo = "\n".join(linhas[ini:]).strip()
    return titulo, autor, data, url, corpo

def main():
    if len(sys.argv) < 3:
        print("uso: python converte_posts.py <entrada> <saida>")
        sys.exit(1)

    entrada, saida = Path(sys.argv[1]), Path(sys.argv[2])
    saida.mkdir(parents=True, exist_ok=True)
    arquivos = sorted(entrada.glob("*.md"))
    if not arquivos:
        print("Nenhum .md em", entrada)
        sys.exit(1)

    rel, redir, probs_arqs = [], [], []

    for arq in arquivos:
        titulo, autor, data, url, corpo = processar(arq.read_text(encoding="utf-8"))
        probs = []

        if not titulo: probs.append("sem titulo")
        if not autor:  probs.append("sem autor")
        if not data:   probs.append("sem data")

        ids, faltando = resolver_autor(autor or "")
        if faltando:
            probs.append("autor(es) nao mapeado(s): " + ", ".join(faltando))

        d = parse_data(data or "")
        if not d:
            probs.append("data nao reconhecida: " + str(data))
        iso = d.isoformat() if d else "2000-01-01"

        slug = slugify(titulo or arq.stem)
        secao = classificar_secao(titulo or "", corpo)

        # monta autores YAML
        if ids:
            autores_yaml = "\n" + "\n".join("  - " + i for i in ids)
        else:
            autores_yaml = "\n  - rodrigo-medeiros"  # fallback + rascunho

        fm = ["---",
              'titulo: "%s"' % (titulo or "").replace('"', '\\"'),
              "autores:" + autores_yaml,
              "publicado_em: " + iso,
              'secao: ' + secao,
              "tags: []",
              "arquivo: true",
        ]
        if url:
            fm.append('medium_url_original: "%s"' % url)
            fm.append("publicado_originalmente_em: " + iso)
        if not ids:
            fm.append("rascunho: true")
        fm += ["---", "", corpo, ""]

        nome_saida = slug + ".md"
        (saida / nome_saida).write_text("\n".join(fm), encoding="utf-8")

        # redirect Medium → /posts/<slug>
        if url:
            try:
                path = "/" + url.split("medium.com/", 1)[1].split("/", 1)[1]
                redir.append("%s  /posts/%s  301" % (path, slug))
            except IndexError:
                pass

        status = "OK" if not probs else "REVISAR"
        rel.append("[%s] %s  →  %s" % (status, arq.name, nome_saida))
        for p in probs:
            rel.append("        ! " + p)
        if probs:
            probs_arqs.append(arq.name)

    (saida / "_relatorio.txt").write_text(
        "Convertidos: %d\nA revisar: %d\n\n" % (len(arquivos), len(probs_arqs))
        + "\n".join(rel), encoding="utf-8")
    (saida / "_redirects.txt").write_text("\n".join(redir), encoding="utf-8")

    print("Pronto! %d arquivos convertidos em %s" % (len(arquivos), saida))
    print("  a revisar: %d  (ver _relatorio.txt)" % len(probs_arqs))
    print("  redirects: %d  (ver _redirects.txt)" % len(redir))
    print("\nProximo passo:")
    print("  Mova os .md de %s para src/content/posts/" % saida)

if __name__ == "__main__":
    main()