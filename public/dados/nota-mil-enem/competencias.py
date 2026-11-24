"""Capítulo 3 · média de cada competência da redação (C1 a C5) no Nordeste e no resto do país, por ano.

Mesmas regras de analise.py: estado da prova, redação válida ("sem problemas"), Nordeste = AL BA CE MA PB PE PI RN SE.
Saída: dados/competencias_regiao.csv e um resumo impresso."""
import glob
import os

import pandas as pd

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados')
NE = {'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'}

t = pd.concat(pd.read_csv(f, dtype={'faixa': str, 'status': str}) for f in sorted(glob.glob(f'{D}/agregado_*.csv')))
t['status'] = t['status'].astype(str)
valida = ((t.ano <= 2014) & (t.status == '7')) | ((t.ano >= 2015) & (t.status == '1'))
v = t[valida & (t.faixa != 'sem_nota') & (t.uf != 'NA')].copy()
v['regiao'] = v.uf.map(lambda u: 'Nordeste' if u in NE else 'Resto do país')
cols = ['n', 'soma_nota'] + [f'soma_c{i}' for i in range(1, 6)]
g = v.groupby(['ano', 'regiao'])[cols].sum()
out = pd.DataFrame({'n': g.n, 'nota': g.soma_nota / g.n})
for i in range(1, 6):
    out[f'c{i}'] = g[f'soma_c{i}'] / g.n
out = out.reset_index()
out.to_csv(f'{D}/competencias_regiao.csv', index=False)

if __name__ == '__main__':
    pd.set_option('display.width', 250)
    p = out.pivot(index='ano', columns='regiao')
    dif = pd.DataFrame({c: p[c]['Nordeste'] - p[c]['Resto do país'] for c in ['nota', 'c1', 'c2', 'c3', 'c4', 'c5']})
    print('Média (Nordeste − resto do país), pontos:')
    print(dif.round(1).to_string())
    print('\nMédias do Nordeste:')
    print(p.xs('Nordeste', axis=1, level=1)[['nota', 'c1', 'c2', 'c3', 'c4', 'c5']].round(1).to_string())
    print('\nMédias do resto do país:')
    print(p.xs('Resto do país', axis=1, level=1)[['nota', 'c1', 'c2', 'c3', 'c4', 'c5']].round(1).to_string())
