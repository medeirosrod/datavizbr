---
titulo: "Como fizemos o mapa interativo que te coloca no epicentro da epidemia de Covid-19 no Brasil"
descricao: Os bastidores técnicos e criativos do mapa interativo No Epicentro, que mostra o raio de mortes por Covid-19 ao redor do usuário.
autores:
  - rodrigo-menegat-schuinski
publicado_em: 2020-07-24
secao: bastidores
tags: ["COVID-19", "Clima", "Dados", "Dataviz", "Educação"]
medium_url_original: "https://medium.com/datavizbr/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-19-no-brasil-4ce949a9183b"
publicado_originalmente_em: 2020-07-24
capa: ../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/01.png
capa_alt: Capa do post Como fizemos o mapa interativo que te coloca no epicentro da epidemia de Covid-19 no Brasil
---

*por Rodrigo Menegat, Tiago Maranhão e Vinicius Sueiro*

![Captura de tela do projeto No Epicentro mostrando um círculo vermelho ao redor de um ponto de referência em um mapa escuro pontilhado de branco, com uma caixa de texto explicando que todo mundo que vive dentro do círculo, desenhado com raio de 2,2 km, teria morrido](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/02.jpeg)

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

![Mapa dos Estados Unidos formado por manchas verdes que representam apenas as áreas onde Hillary Clinton teve mais votos que Donald Trump, com o restante do território apagado em cinza claro](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/01.png)

![Mapa dos Estados Unidos formado por manchas vermelhas que representam apenas as áreas onde Donald Trump teve mais votos que Hillary Clinton, com o restante do território apagado em cinza claro](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/03.png)

*Mapa que apaga as áreas dos Estado Unidos onde Donald Trump teve mais votos que Hillary Clinton*

- O projeto "Aqui não mora ninguém" da Plano C, mostrando áreas desabitadas do Brasil

![Mapa do Brasil do projeto Aqui não mora ninguém, da Plano C](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/04.png)

*As áreas laranja representam regiões desabitadas do Brasil*

![Mapa 3D do The Pudding em que barras sobre o mapa representam a quantidade de pessoas que moram em cada área](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/05.png)

*Mapa de densidade populacional produzida pela empresa americana de jornalismo de dados The Pudding*

![Gráfico interativo do Nexo comparando a densidade populacional de cidades brasileiras](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/06.png)

*A mesma quantidade de pessoas mora na área azul e na área vermelha*

- O Racial Dot Map (Universidade de Virgínia), onde cada ponto representa uma pessoa

![Racial Dot Map, mapa dos Estados Unidos formado por pontos coloridos](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/07.png)

*Cada ponto representa uma pessoa. Cada cor, uma raça.*

- Reportagens personalizadas do NYTimes sobre temperatura e poluição na cidade do leitor

![Reportagem do The New York Times sobre o aumento de temperatura na cidade do leitor](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/08.png)

*Gráfico personalizado mostra o crescimento da temperatura na cidade natal do leitor*

![Reportagem do The New York Times sobre poluição atmosférica com micropartículas representadas por círculos](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/09.png)

*A quantidade de micropartículas de poluição no ar da cidade onde o usuário mora é representada por pequenos círculos*

![Fotografia aérea de covas abertas em cemitério de São Paulo durante a pandemia](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/10.jpeg)

*Covas abertas em São Paulo. Foto: José Antonio de Moraes/Anadolu Agency/Getty*

![Página do Memorial Inumeráveis, que reúne obituários de vítimas da Covid-19](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/11.png)

*Projeto reúne obituários de vítimas da Covid-19 no Brasil*

**Brainstorming**

Foram listadas 11 propostas diferentes, incluindo realidade aumentada, modelos 3D, cemitérios em espaços públicos e distribuição de pontos. No final, foram escolhidos elementos de múltiplas propostas.

![Esboços à mão que listam as onze propostas consideradas para o projeto](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/12.jpeg)

*Esboço que lista onze projetos que consideramos antes de escolher o formato final*

**Algoritmo**

O algoritmo final calcula um círculo ao redor das coordenadas do usuário, aumentando o raio progressivamente até que a população dentro do círculo alcance entre 90% e 110% do total de mortos por Covid-19 no Brasil. A população foi calculada a partir dos setores censitários do IBGE.

![Mapa com retângulos em tons de azul representando a grade estatística do IBGE](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/13.png)

*Cada retângulo na imagem acima é um item da grade estatística do IBGE. Quanto mais escuro, mais pessoas moram naquela área.*

![Mapa com polígonos representando setores censitários do IBGE](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/14.png)

*Os setores censitários costumam ser menores em áreas muito povoadas e maiores em áreas com menor densidade demográfica.*

![Diagrama do primeiro algoritmo, que selecionava setores censitários vizinhos sucessivamente](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/15.jpeg)

*Representação visual do algoritmo: de vizinho em vizinho, tentávamos chegar ao total de mortos*

![Mapa com uma área vermelha de forma irregular sobre o bairro da Barra Funda, em São Paulo](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/16.jpeg)

*Resultado do algoritmo no bairro da Barra Funda, em São Paulo: como explicar para o leitor qual é o sentido dessa área vermelha estranha?*

![Mapa com um círculo vermelho centrado no Centro Histórico de Recife](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/17.png)

*O raio de mortes a partir do Centro Histórico de Recife. O formato circular passa a mensagem de forma mais efetiva do que no exemplo anterior.*

**Desafios de performance**

O tempo de execução inicial era de 30 segundos. Com otimizações usando as bibliotecas Feather (leitura rápida de arquivos), PyGEOS (operações vetorizadas geométricas) e Rtree (índices espaciais), o tempo caiu para menos de 3 segundos.

![Gráfico comparando o tempo de leitura de arquivos nos formatos shapefile e feather](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/18.png)

*Comparação entre o tempo necessário para ler um arquivo no formato shapefile e no formato feather: o último é quase três vezes mais rápido.*

![Diagrama de um índice espacial do tipo r-tree, com polígonos menores encapsulados por polígonos maiores](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/19.png)

*Um tipo específico de índice espacial chamado r-tree. Veja como os polígonos menores, vermelhos, são encapsulados por polígonos maiores*

![Gráfico mostrando a queda do tempo de execução do código após as otimizações](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/20.png)

*Depois de toda a otimização, o tempo de execução do código caiu de meio minuto para menos de três segundos*

**200 milhões de pontos**

Em vez de gerar apenas pontos dentro do círculo, a equipe gerou previamente uma camada com 190 milhões de pontos — um para cada habitante do Brasil em 2010 — processados a partir dos setores censitários do IBGE. Os dados resultantes (cerca de 23 gigabytes) foram convertidos para tilesets usando o tippecanoe do Mapbox.

![Animação sobre a escolha das tecnologias da interface visual do projeto](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/21.gif)

*Decidir como implementar a interface visual do projeto não foi simples*

![Triângulo bege dentro de um retângulo azul com um ponto vermelho, ilustrando probabilidades geométricas](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/22.png)

*Quais as chances de o ponto vermelho cair na região azul ou na região amarela?*

![Simulações com quantidades crescentes de pontos gerados aleatoriamente dentro do retângulo](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/23.png)

*Quanto mais pontos gerados, mais próxima a distribuição fica da probabilidade teórica*

![Sequência de oito pequenos mapas mostrando o processo de gerar pontos aleatórios dentro do bounding box de um setor censitário até estimar corretamente sua população real](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/24.png)

*Note como o valor de pontos dentro do setor ficou próximo do real: de 866 pontos esperados, 862 caíram dentro.*

![Captura de tela de um protótipo em desenvolvimento mostrando pontos vermelhos preenchendo os setores censitários ao redor de Palhoça, Santa Catarina, com um log de execução do script à esquerda](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/25.png)

*Um dos primeiros protótipos, destacando as mortes em torno de um ponto no município de Palhoça, SC*

![Protótipo de mapa mostrando uma nuvem densa de pontos vermelhos representando a população ao redor do bairro Vila Matilde, em São Paulo](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/26.png)

*Protótipo de mapa com que exibe um ponto para cada habitante do Brasil, em vez de exibir apenas um ponto para cada vítima da Covid-19*

![Notebook antigo com um cooler improvisado feito de peças de Lego](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/27.png)

*Um cooler feito de peças de Lego evitou que esse pobre computador entrasse em combustão*

**Lições aprendidas**

1. Especializar tarefas, mas coletivizar debates: divisão rigorosa do trabalho, mas com liberdade para sugestões sobre tópicos alheios.

2. Brainstorming eterno: manter um ambiente de ideação constante com referências, sugestões e debates ao longo de todo o processo.

![Galeria de mídia do grupo de WhatsApp da equipe, com referências, testes e memes](../../assets/blog/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-1/28.png)

*A mídia compartilhada no grupo de WhatsApp: referências, testes, memes, cursos e árvores secas*

3. Aprender no processo: disposição para mergulhar em temas novos rapidamente. O grupo se autodenominou "Irresponsáveis Motivados". Como disse a equipe: "Feito é melhor que perfeito."

Os dados de mortes vieram do Brasil.io, mantido por Álvaro Justen e voluntários. O código-fonte do projeto é aberto.

---

*Esse post foi originalmente postado no [Medium do datavizbr](https://medium.com/datavizbr/como-fizemos-o-mapa-interativo-que-te-coloca-no-epicentro-da-epidemia-de-covid-19-no-brasil-4ce949a9183b) e pode ser encontrado no link acima.*
