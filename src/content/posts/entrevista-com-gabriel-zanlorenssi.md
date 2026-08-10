---
titulo: "Entrevista com Gabriel Zanlorenssi"
descricao: Gabriel Zanlorenssi, do Nexo Jornal, compara ggplot2 e D3 e dá dicas de ferramentas para quem está começando em dataviz.
autores:
  - rodrigo-medeiros
publicado_em: 2019-07-24
secao: panorama
tags: ["Cultura", "Dados", "Dataviz", "Design", "Educação"]
medium_url_original: "https://medium.com/datavizbr/entrevista-com-gabriel-zanlorenssi-16a977b02824"
publicado_originalmente_em: 2019-07-24
capa: ../../assets/blog/entrevista-com-gabriel-zanlorenssi/01.jpeg
capa_alt: Capa do post Entrevista com Gabriel Zanlorenssi
---

Agora em julho de 2019 começamos uma série de novos quadros no datavizbr. Traduções, entrevistas e tutoriais sobre a área de visualização de dados no Brasil serão parte dessa nova articulação com designers, jornalistas e programadores.

Para iniciar essa leva de novos textos, começamos com uma entrevista com Gabriel Zanlorenssi que é cientista de dados do Nexo Jornal e mestrando em Ciência Política na USP. Graduado em Ciências Sociais, na mesma universidade, e programador em R.

**Você poderia me contar um pouco da sua trajetória com visualização de dados?**

Eu sempre gostei muito de mapas e gráficos. Desde criança, colecionava atlas e almanaques, mas foi apenas durante a faculdade que aprendi a fazer minhas próprias visualizações. Sou graduado em Ciências Sociais na USP e tive oportunidade de fazer uma iniciação científica, na qual aprendi a usar o Stata.

Terminei a graduação em 2016 e ingressei no mestrado em Ciência Política em 2017, também na USP. Logo no primeiro semestre, fiz uma matéria inteiramente voltada à análise de dados em R e assim fiz minha "conversão" do Stata para o R.

Nessa época, costumava fazer algumas visualizações e postar nas minhas redes sociais. Em uma dessas visualizações que postei, um amigo em comum com uma editora do Nexo Jornal a marcou na minha publicação. Ela gostou das coisas que eu postava e, como na época havia uma vaga aberta para cientista de dados no jornal, surgiu um convite para uma entrevista.

Em visualização de dados quantitativos, penso que estatística e programação são as principais ferramentas. Leva tempo e sempre repito que não se pode desanimar no primeiro mês.

**Qual foi a experiência que você teve com D3 e com ggplot2? Quais as grandes diferenças entre eles?**

O ggplot2 é a principal biblioteca gráfica do R e me arrisco a dizer que talvez seja a principal dentre todas as linguagens. Ele se propõe literalmente a ser uma gramática de como se fazer gráficos. Na minha opinião pessoal, o ggplot2 é mais centrado nos dados do que na forma, o que permite você pensar mais sobre a natureza do seu dado. Aprendi o ggplot2 junto com o R e o utilizo para quase 100% das visualizações que produzo atualmente.

O ggplot2 faz parte de um projeto maior chamado Tidyverse, liderado por Hadley Wickham e vários outros profissionais. O conjunto de pacotes que compõem o Tidyverse revolucionou o jeito que o R funciona.

Já o D3, referência a data-driven documents, é uma biblioteca de JavaScript voltada para o desenvolvimento de visualizações para web. O D3 é extremamente customizável e muitos atributos do gráfico devem ser definidos manualmente. Isso por um lado deixa o processo bem mais trabalhoso e os códigos mais longos mas por outro as possibilidades são infinitas.

**Em quais situações você acha melhor utilizar o ggplot2 e em quais o D3?**

Quando a visualização é uma imagem estática, o ggplot2 é uma solução eficiente e rápida. Quando predominam recursos de interatividade, como tooltips, botões, gráficos reativos, entre outros, acho que o D3 é uma melhor opção.

Em geral, não precisamos usar gráficos interativos para tudo. Na maioria dos casos, um gráfico estático consegue comunicar os dados muito bem.

**Qual é a maior dificuldade em trabalhar com o D3 na realidade de uma redação de jornal?**

Pensando em um veículo de imprensa, com um site estruturado e com publicador, colocar um gráfico com JavaScript no meio de uma matéria ou interativo não é uma tarefa tão simples. O código precisa conversar com o restante do site. E, claro, isso tudo sem mencionar a escassez de profissionais que tenham um bom domínio do D3.

**Quais outros frameworks para criação de gráficos você pode sugerir para quem está iniciando em visualização de dados?**

Para quem está começando, uma boa opção podem ser ferramentas online que produzem gráficos sofisticados sem nenhuma necessidade de conhecimento de programação. Recomendo particularmente o Flourish e o Raw Graphs. Pode-se baixar o gráfico produzido como imagem (png) ou arquivo de vetores (svg).

Também há, para o próprio ggplot2 mesmo, uma extensão chamada esquisse, que permite a criação de gráficos no R arrastando caixas e clicando botões.

---

*Esse post foi originalmente postado no [Medium do datavizbr](https://medium.com/datavizbr/entrevista-com-gabriel-zanlorenssi-16a977b02824) e pode ser encontrado no link acima.*