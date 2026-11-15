"""Agrega a redação do Enem de um ano, lendo o CSV do Inep em fluxo (sem gravar o zip) e guardando só contagens.

Uso: python3 enem_agg.py ANO SAIDA_DIR
Saída: SAIDA_DIR/agregado_ANO.csv com uma linha por (ano, uf_prova, status_redacao, faixa) e as colunas
  n, soma_nota, soma_c1..soma_c5  (somas de nota e de competências, para médias depois).
faixa: piso da nota em centenas (0, 100, ..., 900) e 1000 para a nota máxima; 'sem_nota' quando não há nota.
Regra de "presente na redação": TP_STATUS_REDACAO preenchido. Estado: SG_UF_PROVA (UF onde fez a prova).
Fonte: https://download.inep.gov.br/microdados/microdados_enem_ANO.zip"""
import sys, time
import numpy as np
import pandas as pd

sys.path.insert(0, '.')
from httpzip import open_remote_zip, abrir_entrada

ano = int(sys.argv[1])
saida = sys.argv[2]
url = f"https://download.inep.gov.br/microdados/microdados_enem_{ano}.zip"
z = open_remote_zip(url, buffer_mb=16)
alvo = "RESULTADOS" if ano >= 2024 else "MICRODADOS"
entrada = next(i for i in z.infolist() if i.filename.upper().rsplit('/',1)[-1].startswith(alvo) and i.filename.lower().endswith('.csv'))
print(f"[{ano}] lendo {entrada.filename} ({entrada.compress_size/1e6:.0f} MB comprimido)", flush=True)

cols = ['NU_ANO', 'SG_UF_PROVA', 'TP_STATUS_REDACAO', 'NU_NOTA_REDACAO',
        'NU_NOTA_COMP1', 'NU_NOTA_COMP2', 'NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5']
acc = []
linhas = 0
t0 = time.time()
with abrir_entrada(z, entrada) as f:
    for ch in pd.read_csv(f, sep=';', encoding='latin-1', usecols=cols, dtype=str, chunksize=400_000):
        linhas += len(ch)
        ch = ch[ch['TP_STATUS_REDACAO'].notna()].copy()
        num = {c: pd.to_numeric(ch[c], errors='coerce') for c in cols[3:]}
        nota = num['NU_NOTA_REDACAO']
        faixa = pd.Series('sem_nota', index=ch.index, dtype=object)
        ok = nota.notna()
        faixa[ok] = np.where(nota[ok] >= 1000, '1000', (np.floor(nota[ok] / 100) * 100).astype(int).astype(str))
        g = pd.DataFrame({
            'ano': ano,
            'uf': ch['SG_UF_PROVA'].fillna('NA'),
            'status': ch['TP_STATUS_REDACAO'],
            'faixa': faixa,
            'nota': nota.fillna(0), 'c1': num['NU_NOTA_COMP1'].fillna(0), 'c2': num['NU_NOTA_COMP2'].fillna(0),
            'c3': num['NU_NOTA_COMP3'].fillna(0), 'c4': num['NU_NOTA_COMP4'].fillna(0), 'c5': num['NU_NOTA_COMP5'].fillna(0),
        })
        acc.append(g.groupby(['ano', 'uf', 'status', 'faixa'], as_index=False).agg(
            n=('nota', 'size'), soma_nota=('nota', 'sum'), soma_c1=('c1', 'sum'), soma_c2=('c2', 'sum'),
            soma_c3=('c3', 'sum'), soma_c4=('c4', 'sum'), soma_c5=('c5', 'sum')))
        if (linhas // 400_000) % 5 == 0:
            print(f"[{ano}] {linhas:,} linhas lidas, {time.time()-t0:.0f}s", flush=True)

tab = pd.concat(acc).groupby(['ano', 'uf', 'status', 'faixa'], as_index=False).sum()
tab.to_csv(f"{saida}/agregado_{ano}.csv", index=False)
mil = int(tab.loc[tab['faixa'] == '1000', 'n'].sum())
print(f"[{ano}] FIM: {linhas:,} linhas no arquivo, {int(tab['n'].sum()):,} com redação, {mil} notas mil, {time.time()-t0:.0f}s", flush=True)
