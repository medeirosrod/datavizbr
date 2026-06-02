---
titulo: "Visualizando a composição ministerial do Governo Lula"
autores:
  - adolfo-guimaraes
publicado_em: 2023-01-20
secao: bastidores
tags: []
arquivo: true
medium_url_original: "https://medium.com/datavizbr/visualizando-a-composição-ministerial-do-governo-lula-d0c92ed42378"
publicado_originalmente_em: 2023-01-20
rascunho: true
---

Nesse texto vou explorar a construção de uma visualização para mostrar a composição ministerial do terceiro governo Lula. O objetivo da visualização é mostrar a composição a partir de três variáveis: partidos, gênero e raça.

**Dados utilizados**

Os dados utilizados foram mapeados a partir de entrevistas e bases de dados. A lista de ministros empossados foi retirada do site do G1. Para as informações de raça, foram utilizadas duas fontes. As autodeclarações das pessoas pretas e pardas foram mapeadas pelo site Alma Preta. Para os demais que não foram mapeados, foi feita uma busca nos dados do TSE via o site da Base dos Dados. Os ministros que não foram classificados nesses passos, receberam o label "Sem informação".

Os dados estão organizados em cinco atributos: nome, ministério, partido, gênero, info_raça. Todos categóricos.

**Aspectos da Visualização**

**Gráfico principal**

Para visualizar a distribuição de partidos foi utilizado um Donut Chart que é semelhante a um gráfico de pizza, mas com uma área central. Esses dois tipos de gráficos têm como objetivo mostrar parte de um todo. Os ministérios estão distribuídos em 9 partidos e uma categoria sem partido. A proposta era mostrar, de forma geral, como está distribuído o ministério do governo Lula — quais partidos compõem boa parte do ministério e aqueles que participam com menos ministros.

**Quantificando os arcos**

Como o tipo de gráfico utilizado não é muito apropriado para comparar valores, os valores foram quantificados por símbolos (círculos alinhados aos arcos). Essa abordagem só faz sentido quando temos um número pequeno em cada categoria. Com isso, é possível ver a quantidade exata de ministros dentro de cada partido.

**Ícones utilizados**

Cada ministro é representado por um ícone (círculo). Há uma diferença que permite identificar homens e mulheres: no ícone para mulheres foi dado um destaque com um círculo pontilhado ao redor do círculo principal. Foram evitados ícones representativos de homens e mulheres para não propagar estereótipos.

**Cores utilizadas**

Para a representação das cores dos partidos foi utilizada como base uma paleta de cores padrão do d3.js, ajustada em uma ferramenta de acessibilidade para verificar a acessibilidade das cores para pessoas com deficiência visual. Para as informações de gênero e raça, foram utilizadas cores distintas que atendem critérios de acessibilidade.

**Rótulos e Interação**

Os rótulos foram utilizados para identificar cada partido no arco e mostrar resumos percentuais de mulheres e pessoas negras e indígenas. Quando o mouse é passado nos partidos, esse percentual é atualizado por partido.

A visualização possui interações para exibir informações mais completas quando o usuário quiser: visualizar o nome de todos os ministros, visualizar os ministros por partido, e visualizar as informações de um ministro específico.

Toda visualização foi criada utilizando d3.js e pode ser acessada no Observable HQ do autor.
