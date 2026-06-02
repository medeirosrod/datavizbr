---
titulo: "Como fizemos o mapa interativo que te coloca no epicentro da epidemia de Covid-19 no Brasil"
autores:
  - rodrigo-menegat-schuinski
publicado_em: 2020-07-24
secao: bastidores
tags: []
arquivo: true
medium_url_original: "https://medium.com/datavizbr/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-19-no-brasil-4ce949a9183b"
publicado_originalmente_em: 2020-07-24
rascunho: true
---

*por Rodrigo Menegat, Tiago Maranhão e Vinicius Sueiro*

Se todos os mortos pela Covid-19 no Brasil fossem seus vizinhos, seu bairro provavelmente desapareceria do mapa. É possível que até a sua cidade inteira sumisse.

Uma parceria entre o Google News Initiative e a Agência Lupa mostra na prática como seria essa realidade. Usando a localização do usuário, dados do Censo de 2010 e mapas de rua, esta reportagem interativa mostra qual seria o raio da devastação caso o epicentro da epidemia no Brasil fosse a casa do leitor.

**Conceito: Uma tragédia invisível**

No momento em que começamos a escrever esse texto, 58.390 brasileiros haviam morrido vítimas do novo coronavírus. A realidade, porém, independe de onde você mora: os mortos estão dentro de hospitais espalhados por todo o território nacional, mas não os vemos.

Esse projeto surgiu da seguinte indagação: como fazer para que as pessoas passem a enxergar esses mortos?

**Referências familiares**

60 mil pessoas mortas. É como se um Estádio do Arruda lotado, no Recife, desaparecesse. A lógica vale para quem está em qualquer lugar: quanto mais familiar a unidade de medida, mais fácil compreender a dimensão da epidemia.

A ideia fundamental deste projeto é fazer com que as vítimas da Covid-19 se tornem, subitamente, íntimas do usuário.

**Inspirações**

- Um projeto do The New York Times que apaga regiões dos EUA de acordo com resultados eleitorais
- O projeto "Aqui não mora ninguém" da Plano C, mostrando áreas desabitadas do Brasil
- O Racial Dot Map (Universidade de Virgínia), onde cada ponto representa uma pessoa
- Reportagens personalizadas do NYTimes sobre temperatura e poluição na cidade do leitor

**Brainstorming**

Foram listadas 11 propostas diferentes, incluindo realidade aumentada, modelos 3D, cemitérios em espaços públicos e distribuição de pontos. No final, foram escolhidos elementos de múltiplas propostas.

**Algoritmo**

O algoritmo final calcula um círculo ao redor das coordenadas do usuário, aumentando o raio progressivamente até que a população dentro do círculo alcance entre 90% e 110% do total de mortos por Covid-19 no Brasil. A população foi calculada a partir dos setores censitários do IBGE.

**Desafios de performance**

O tempo de execução inicial era de 30 segundos. Com otimizações usando as bibliotecas Feather (leitura rápida de arquivos), PyGEOS (operações vetorizadas geométricas) e Rtree (índices espaciais), o tempo caiu para menos de 3 segundos.

**200 milhões de pontos**

Em vez de gerar apenas pontos dentro do círculo, a equipe gerou previamente uma camada com 190 milhões de pontos — um para cada habitante do Brasil em 2010 — processados a partir dos setores censitários do IBGE. Os dados resultantes (cerca de 23 gigabytes) foram convertidos para tilesets usando o tippecanoe do Mapbox.

**Lições aprendidas**

1. Especializar tarefas, mas coletivizar debates: divisão rigorosa do trabalho, mas com liberdade para sugestões sobre tópicos alheios.

2. Brainstorming eterno: manter um ambiente de ideação constante com referências, sugestões e debates ao longo de todo o processo.

3. Aprender no processo: disposição para mergulhar em temas novos rapidamente. O grupo se autodenominou "Irresponsáveis Motivados". Como disse a equipe: "Feito é melhor que perfeito."

Os dados de mortes vieram do Brasil.io, mantido por Álvaro Justen e voluntários. O código-fonte do projeto é aberto.
