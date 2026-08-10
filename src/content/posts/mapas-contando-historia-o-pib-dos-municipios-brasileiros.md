---
titulo: "Mapas contando história: o PIB dos municípios brasileiros"
descricao: Mapas de clusterização revelam os seis perfis econômicos dos municípios brasileiros a partir dos dados de PIB do IBGE.
autores:
  - fernando-barbalho
publicado_em: 2020-08-03
secao: bastidores
tags: ["Dados", "Dataviz", "Mapa", "Urbanismo"]
medium_url_original: "https://medium.com/datavizbr/mapas-contando-história-o-pib-dos-municípios-brasileiros-aebb82f06086"
publicado_originalmente_em: 2020-08-03
capa: ../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/01.jpeg
capa_alt: "Capa do post Mapas contando história: o PIB dos municípios brasileiros"
---

Riqueza, pobreza, territórios maiores do que países, municípios que são quase apenas pequenos povoados, populações enormes, agropecuária, indústria e serviço. O que todos esses elementos tem a nos dizer quando estão presentes em mapas que mostram os municípios do Brasil?

Usando uma escala única para as variáveis dos componentes do PIB, o próprio PIB e o PIB per capita dos municípios, foi rodado um algoritmo de formação de agrupamentos (clusters). A melhor combinação testada levou à formação de seis clusters. Os dados são de 2017, fornecidos pelo IBGE. Os mapas foram feitos com o suporte do pacote geobr na linguagem R.

Antes de detalhar o que caracteriza os agrupamentos, veja como fica o mapa do Brasil com cada município representado por sua posição nos agrupamentos.

![Mapa do Brasil com cada município colorido de acordo com seu agrupamento econômico](../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/02.png)

**Os seis agrupamentos**

Os agrupamentos 1, 2 e 3 (cores mais frias) são os municípios com as piores combinações das variáveis econômicas. O agrupamento 4 se destaca por ter um elevado PIB Per capita. O grupo 5 se destaca por um elevado PIB gerado pela atividade agropecuária. O agrupamento 6 é formado pelos municípios que têm todas as variáveis elevadas para o caso brasileiro.

![Gráfico mostrando a distribuição de cada variável que forma os agrupamentos](../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/03.png)

A maior contribuição ao PIB vem do setor de serviços. Com contribuições equivalentes a um terço do setor de serviços aparecem em seguida indústria e administração. Com contribuição bem menor está o setor agropecuário.

![Gráfico da contribuição de cada segmento econômico ao PIB total](../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/04.png)

**Nordeste e Go-West**

![Mapa do Brasil exibindo as cores que identificam cada agrupamento](../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/05.png)

O Nordeste é praticamente dominado pelas cores mais frias, que caracterizam os municípios em situação econômica mais complicada. O agrupamento 6 está presente apenas nas capitais e em mais alguns municípios próximos a Recife e Salvador.

![Detalhamento da região Nordeste com a distribuição de clusters](../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/06.png)

Outro achado: "Go West" parece ser o lema da economia atual. Nas vastas regiões do Centro-Oeste concentra-se o agrupamento 5, com PIB elevado do setor agropecuário. Essa expansão econômica das novas fronteiras agrícolas está sendo feita às custas de forte desmatamento.

![Mapa do Centro-Oeste e Pará mostrando predominância do cluster com foco no agronegócio](../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/07.png)

**Minas Gerais e São Paulo**

![Mapa de Minas Gerais mostrando como os clusters econômicos formam clusters territoriais](../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/08.png)

Minas Gerais é conhecido por ser o estado que sintetiza o Brasil. Os clusters econômicos formam clusters territoriais. As cidades nos clusters de cores mais frias estão mais ao Norte. Os tons mais esverdeados concentram-se no Oeste.

São Paulo mostra que dinheiro chama dinheiro, dada a concentração territorial dos municípios dourados. Os municípios em amarelo representam elevados valores de PIB, PIB per capita e dos três componentes do PIB mais importantes. Apesar de pequeno em número e em termos territoriais, o agrupamento amarelo representa municípios de elevada população.

![Mapa de São Paulo mostrando a concentração territorial dos municípios com elevado PIB](../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/09.png)

**Outros mapas e outras histórias**

O mapa Go-West pode ser contrastado com o que está presente nesse tuíte do professor Raoni Rajão, sobre um artigo que indica que, nas regiões das novas fronteiras agrícolas, a expansão econômica está sendo feita às custas de forte desmatamento.

![Mapa do estudo publicado na Science relacionando desmatamento de propriedades rurais às exportações de soja e carne na Amazônia e no Cerrado, compartilhado em tuíte do professor Raoni Rajão](../../assets/blog/mapas-contando-historia-o-pib-dos-municipios-brasileiros/10.png)

*Imagem do tuíte de [Raoni Rajão (@RajaoPhD)](https://x.com/RajaoPhD/status/1283844944357097473), 16 de julho de 2020.*

*Fernando Barbalho — Doutor em Administração pela UnB (2014). Pesquisa e implementa produtos para transparência no setor público brasileiro. Usa R nos finais de semana para investigar perguntas que fogem às finanças públicas.*

---

*Esse post foi originalmente postado no [Medium do datavizbr](https://medium.com/datavizbr/mapas-contando-história-o-pib-dos-municípios-brasileiros-aebb82f06086) e pode ser encontrado no link acima.*