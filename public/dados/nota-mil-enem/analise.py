"""Capítulo 3 · Nordeste em dados · "As redações nota mil do Enem": análise sobre os agregados.

Entrada: dados/agregado_AAAA.csv (gerados por enem_agg.py a partir dos microdados do Inep).
Saída: tabelas em dados/ (serie_regiao.csv, serie_uf.csv) e um resumo impresso.

Regras de contagem (iguais para todos os anos):
- Estado = UF onde o participante fez a prova (SG_UF_PROVA), não a da escola.
- Redação válida = situação "sem problemas": código 1 de 2015 em diante, código 7 em 2013 e 2014
  (nesses dois anos o dicionário usa outra codificação: 6 = ausente, 7 = presente e conforme).
- Nota alta = nota da redação >= 900 (faixas 900 e 1000). Nota mil = 1000.
- Nordeste = AL, BA, CE, MA, PB, PE, PI, RN, SE.
"""
import glob
import os
import sys

import pandas as pd

AQUI = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(AQUI, 'dados')
NE = {'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'}

t = pd.concat(pd.read_csv(f, dtype={'faixa': str, 'status': str}) for f in sorted(glob.glob(f'{D}/agregado_*.csv')))
t['status'] = t['status'].astype(str)
valida = ((t.ano <= 2014) & (t.status == '7')) | ((t.ano >= 2015) & (t.status == '1'))
v = t[valida & (t.faixa != 'sem_nota') & (t.uf != 'NA')].copy()
v['nordeste'] = v.uf.isin(NE)
v['alta'] = v.faixa.isin(['900', '1000'])
v['mil'] = v.faixa == '1000'


def soma(df, cond=None):
    return (df[cond] if cond is not None else df).groupby('ano').n.sum()


rows = []
for nome, base in (('Brasil', v), ('Nordeste', v[v.nordeste]), ('Resto do país', v[~v.nordeste])):
    r = pd.DataFrame({'validas': soma(base), 'alta900': soma(base, base.alta), 'mil': soma(base, base.mil)})
    r['regiao'] = nome
    r['pct_alta'] = 100 * r.alta900 / r.validas
    r['mil_por_milhao'] = 1e6 * r.mil / r.validas
    rows.append(r.reset_index())
reg = pd.concat(rows)
reg.to_csv(f'{D}/serie_regiao.csv', index=False)

br = reg[reg.regiao == 'Brasil'].set_index('ano')
ne = reg[reg.regiao == 'Nordeste'].set_index('ano')
rs = reg[reg.regiao == 'Resto do país'].set_index('ano')
res = pd.DataFrame({
    'validas_BR': br.validas, 'mil_BR': br.mil,
    'part_NE_%': 100 * ne.validas / br.validas,
    'alta_NE_%': 100 * ne.alta900 / br.alta900,
    'mil_NE_%': 100 * ne.mil / br.mil,
    'pct900_BR': br.pct_alta, 'pct900_NE': ne.pct_alta, 'pct900_resto': rs.pct_alta,
    'razao_NE/resto': ne.pct_alta / rs.pct_alta,
})

uf = v.groupby(['ano', 'uf']).agg(validas=('n', 'sum'))
uf['alta900'] = v[v.alta].groupby(['ano', 'uf']).n.sum()
uf['mil'] = v[v.mil].groupby(['ano', 'uf']).n.sum()
uf = uf.fillna(0).reset_index()
uf['pct_alta'] = 100 * uf.alta900 / uf.validas
uf.to_csv(f'{D}/serie_uf.csv', index=False)

if __name__ == '__main__':
    pd.set_option('display.width', 250)
    pd.set_option('display.max_columns', 30)
    print(res.round(2).to_string())
    ultimo = int(sys.argv[1]) if len(sys.argv) > 1 else uf.ano.max()
    print(f'\nFatia de redações 900+ por UF em {ultimo}:')
    print(uf[uf.ano == ultimo].sort_values('pct_alta', ascending=False)[['uf', 'validas', 'alta900', 'mil', 'pct_alta']].round(2).to_string(index=False))
