---
titulo: "Comparando monografias de uma Universidade brasileira e uma Universidade americana utilizando NLP"
autores:
  - deborah-mesquita
publicado_em: 2017-12-12
secao: bastidores
tags: ["Dados", "Dataviz", "Educação", "Jornalismo"]
medium_url_original: "https://medium.com/datavizbr/comparando-monografias-de-uma-universidade-brasileira-e-uma-universidade-americana-utilizando-nlp-14213b2d7fcd"
publicado_originalmente_em: 2017-12-12
capa: ../../assets/blog/comparando-monografias-de-uma-universidade-brasileira-e-uma-universidade-america/01.png
capa_alt: Capa do post Comparando monografias de uma Universidade brasileira e uma Universidade americana utilizando NLP
---

As pessoas tendem a considerar um trabalho produzido por um estudante de uma Universidade da Ivy League um trabalho muito mais bem produzido do que um feito por um estudante de uma Universidade não tão conceituada.

Mas de que forma esses trabalhos são diferentes? E o que os estudantes podem fazer para produzir trabalhos melhores e consequentemente se destacarem mais?

Medir a qualidade dos trabalhos de uma Universidade é algo bastante complexo e portanto não é o objetivo aqui. Eu sempre tive curiosidade em investigar as diferenças entre trabalhos de instituições diferentes e para iniciar decidi explorar dois fatores envolvendo os trabalhos: a escolha dos temas e a natureza deles.

Neste texto vamos abordar formas de analisar os trabalhos utilizando Processamento de Linguagem Natural. Vamos extrair palavras-chaves utilizando o algoritmo de tf-idf e classificar os trabalhos em clusters utilizando o Latent Semantic Indexing (LSI).

**Os Dados**

O conjunto de dados é composto por resumos (abstracts) de trabalhos de conclusão de curso de estudantes de uma Universidade brasileira (Universidade Federal de Pernambuco) e de uma Universidade americana (Carnegie Mellon). Todos os trabalhos foram feitos por estudantes de graduação em Ciência da Computação.

Segundo o Times Higher Education World University Rankings a Carnegie Mellon tem o 6º melhor programa de Ciência da Computação do mundo, enquanto a Universidade Federal de Pernambuco nem aparece nesse ranking. Já no ranking geral a Carnegie Mellon aparece na posição de número 23, enquanto a UFPE aparece na posição 801+.

Todos os trabalhos foram produzidos entre os anos de 2002 e 2016 e cada linha do dataset possui as seguintes informações: título do trabalho, resumo (abstract) do trabalho, ano de publicação do trabalho, universidade na qual o trabalho foi produzido.

**Etapa 1 — Investigando os temas dos trabalhos**

Para identificar os temas de cada trabalho a primeira estratégia utilizada foi extrair as keywords com o algoritmo de tf-idf.

O tf-idf penaliza as palavras que aparecem muito em um documento e que também aparecem muito nos outros documentos. Ou seja, se uma palavra é muito recorrente em um texto mas também é muito recorrente em outros ela é penalizada; isto quer dizer que essa palavra não serve para caracterizar o determinado texto.

TF(t) = (Número de vezes que o termo t aparece no documento) / (Número total de termos presentes no documento)

IDF(t) = log_e(Número total de documentos / Número de documentos com o termo t presente)

Para cada abstract dos trabalhos das Universidades foram identificadas as 4 palavras com os scores mais altos do tf-idf, utilizando o CountVectorizer e o TfidfTransformer do scikit-learn.

*Keywords da Carnegie Mellon*

**Agrupando os trabalhos em clusters**

A segunda estratégia utilizada para explorar os temas dos trabalhos foi a modelagem de tópicos com o Latent Semantic Indexing (LSI). O algoritmo utiliza os dados do tf-idf e faz uma decomposição de matrizes para agrupar os textos em tópicos.

O tópico que mais diferenciou os trabalhos das Universidades mostrou que os trabalhos da Carnegie Mellon estão mais associados a 'object', 'robot' e 'algorithm' e os trabalhos da UFPE estão mais associados a 'software', 'project' e 'business'.

**Etapa 2 — Investigando a natureza dos trabalhos**

Foram analisados os títulos dos trabalhos para investigar a natureza dos mesmos. Os resultados mostraram diferenças nas especialidades de cada instituição: a Universidade Federal de Pernambuco produz mais trabalhos relacionados a projetos e negócios e a Carnegie Mellon produz mais trabalhos relacionados a robôs e algoritmos.

**Resultados**

A partir da análise foi possível observar que os temas dos trabalhos não diferem muito, mas foi possível visualizar o que parece ser as especialidades de cada instituição. Essa diferença de especialidades não é algo ruim, simplesmente cada universidade é especializada em determinadas áreas.

Um takeaway importante foi de que no Brasil a gente precisa produzir mais conhecimento em vez de só fazer review de literatura.

"It's not enough to be good. In order to be found, you have to be findable." — Austin Kleon

---

*Esse post foi originalmente postado no [Medium do datavizbr](https://medium.com/datavizbr/comparando-monografias-de-uma-universidade-brasileira-e-uma-universidade-americana-utilizando-nlp-14213b2d7fcd) e pode ser encontrado no link acima.*