# Redações nota mil do Enem: método aberto

Material do capítulo 3 de *Nordeste em dados*, do datavizbr. Qualquer pessoa pode refazer a conta.

## Fonte

Microdados do Enem, publicados pelo Inep: `https://download.inep.gov.br/microdados/microdados_enem_AAAA.zip`, de 2013 a 2025. Em 2024 e 2025 as notas ficam no arquivo `RESULTADOS_AAAA.csv`; antes disso, em `MICRODADOS_ENEM_AAAA.csv`.

## O que cada arquivo faz

- `enem_agg.py ANO PASTA`: lê o CSV do ano direto do site do Inep, sem gravar o zip, e grava `PASTA/agregado_ANO.csv` com a contagem de redações por ano, estado da prova, situação da redação e faixa de nota, mais as somas de nota e de cada competência. Usa `httpzip.py`, que abre o zip por pedidos HTTP parciais (precisa de `curl`). O arquivo de 2025 usa compactação Deflate64; para lê-lo é preciso instalar o pacote `inflate64` (PyPI).
- `analise.py`: lê `dados/agregado_*.csv` e gera `dados/serie_regiao.csv` (por região e ano) e `dados/serie_uf.csv` (por estado e ano).
- `competencias.py`: gera `dados/competencias_regiao.csv`, a média de cada competência por região e ano.
- `dados/`: as tabelas já calculadas.

Dependências: Python 3, pandas e numpy.

## Regras de contagem (iguais em todos os anos)

- **Estado:** a UF do local da prova (`SG_UF_PROVA`), não a da escola.
- **Nordeste:** AL, BA, CE, MA, PB, PE, PI, RN e SE.
- **Redação válida:** situação "sem problemas" (`TP_STATUS_REDACAO` igual a 1 de 2015 em diante; igual a 7 em 2013 e 2014, que usam outra codificação: nesses anos, 6 é ausente).
- **Nota alta:** nota da redação de 900 ou mais. **Nota mil:** 1000.

## Conferência

Totais calculados, de 2013 a 2025: 1.237 redações nota mil no Brasil, 384 no Nordeste, 115 no Ceará, 58 em Pernambuco e 51 na Bahia. Esses números coincidem com a reportagem do jornal O Povo de 11/11/2026. As redações com 900 ou mais somam 56.034 em 2013 e 173.543 em 2025, também iguais aos números publicados pela imprensa.

## Limites

O estado é o do local da prova. Não há separação entre rede pública e privada. As diferenças entre competências são de poucos pontos e não indicam causa.
