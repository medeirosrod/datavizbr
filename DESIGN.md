---
name: datavizbr
description: Visualização de dados com sotaque brasileiro
colors:
  terracotta-signal: "#e67e2c"
  terracotta-clay: "#c8651a"
  terracotta-deep: "#9a4a0d"
  terracotta-ink: "#7a3a08"
  peach: "#f4b07a"
  peach-tint: "#fbe3cc"
  ink-purple: "#552b7b"
  ink-purple-deep: "#2a1640"
  lilac: "#b9a3d6"
  lilac-tint: "#e2d2f3"
  rose: "#d98aa6"
  dusk: "#130a1b"
  dusk-raised: "#1c1027"
  wall: "#24142f"
  charcoal-ink: "#1a0f24"
  slate-ink: "#3a2a48"
  mist-ink: "#6b5d76"
  fog-ink: "#948aa0"
  hairline: "#ddd3e5"
  cal: "#f6f2f8"
  cal-shade: "#ebe4f0"
  paper: "#ffffff"
  sky-1: "#4b2c80"
  sky-2: "#8a58ad"
  sky-3: "#d98aa6"
  sky-4: "#f6ab72"
  sky-5: "#e9772a"
  signal-success: "#15be53"
  signal-error: "#c83838"
typography:
  display:
    fontFamily: "Bricolage Grotesque, IBM Plex Sans, system-ui, sans-serif"
    fontSize: "96px"
    fontWeight: 700
    lineHeight: 0.93
    letterSpacing: "-1.1px"
  headline:
    fontFamily: "Bricolage Grotesque, IBM Plex Sans, system-ui, sans-serif"
    fontSize: "64px"
    fontWeight: 700
    lineHeight: 0.96
    letterSpacing: "-0.7px"
  title:
    fontFamily: "Bricolage Grotesque, IBM Plex Sans, system-ui, sans-serif"
    fontSize: "44px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.4px"
  card-title:
    fontFamily: "Bricolage Grotesque, IBM Plex Sans, system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.2px"
  body:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.55
  reading:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.65
  lead:
    fontFamily: "IBM Plex Mono, SFMono-Regular, ui-monospace, Menlo, monospace"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "-0.2px"
  label:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 600
  mono:
    fontFamily: "IBM Plex Mono, SFMono-Regular, ui-monospace, Menlo, monospace"
    fontSize: "12px"
    fontWeight: 400
    letterSpacing: "0.2px"
rounded:
  block: "3px"
  modal: "6px"
  pill: "999px"
spacing:
  space-4: "8px"
  space-8: "16px"
  space-12: "24px"
  space-16: "32px"
  space-24: "48px"
  space-32: "64px"
  space-48: "96px"
components:
  button-primary:
    backgroundColor: "{colors.terracotta-deep}"
    textColor: "#ffffff"
    rounded: "{rounded.block}"
    padding: "0 24px"
    height: "46px"
  button-on-dusk:
    backgroundColor: "{colors.terracotta-signal}"
    textColor: "{colors.dusk}"
    rounded: "{rounded.block}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "inherit"
    rounded: "{rounded.block}"
  wall-block:
    backgroundColor: "{colors.wall}"
    rounded: "{rounded.block}"
    size: "80px"
  card:
    backgroundColor: "{colors.cal}"
    rounded: "{rounded.block}"
---

# Design System: datavizbr

## Overview

**Creative North Star: "Luz Coada"**

A referência é o cobogó, o elemento vazado criado no Recife em 1929. Ele é uma parede de módulos iguais que deixa a luz passar em pedaços regulares, e é a regularidade que permite ler o todo. Uma grade de unidades repetidas que transforma luz em padrão é também uma boa definição de visualização de dados.

No datavizbr, a parede é o acervo. Cada abertura é um texto, na ordem em que foi publicado, e a forma da abertura diz a seção. O mesmo vocabulário de quatro formas reaparece em todas as escalas: na parede da home, nos selos ao lado dos títulos, nos filtros, nos painéis de azulejo, na capa padrão de um texto sem imagem e no friso do rodapé.

Este conceito substitui o "Caderno de Campo", que orientou o site até novembro de 2026.

**Características:**
- A forma vem antes da cor. A seção de um texto se lê pela forma, com ou sem cor.
- A cor é luz. A matéria é escura e fosca; o que brilha é o que passa pelas aberturas.
- Dois cômodos: interior escuro (anoitecer) nos topos de página, exterior claro (cal) no conteúdo.
- Ornamento só existe se carregar dado ou identidade. Nada de decoração solta.
- Pouco texto e de peso: um título grande, rótulos curtos, números.

## The Four Shapes

As quatro formas são a identidade das seções. São desenhadas sobre o mesmo módulo de 80 px, com a mesma margem, e nunca são redesenhadas por página.

| Seção | Forma | Desenho no módulo de 80 px |
|---|---|---|
| Bastidores | Pétala | Quatro lentes que se encontram no centro, apontando para os cantos |
| Panorama | Círculo | Círculo de raio 25 no centro |
| Práticas | Veneziana | Três frestas horizontais de 50 × 12, com cantos arredondados |
| Ensaios | Losango | Quadrado girado, com vértices a 27 do centro |

### Named Rules
**The Shape First Rule.** Toda indicação de seção usa a forma. A cor é reforço e nunca a única pista. Isso vale para selo, filtro, legenda de gráfico e capa padrão.

**The Same Module Rule.** As formas só mudam de escala, nunca de proporção. Um selo de 18 px e um bloco de 80 px usam o mesmo desenho.

## Colors

A paleta mantém as cores de marca do site (terracota e roxo) e ganha um papel novo para cada uma: a terracota é a argila do bloco e a luz do sol; o roxo é a sombra do fim de tarde.

### Terracota
- **Terracotta Signal** (#e67e2c): a cor do sol. Botão sobre fundo escuro, estado ativo, foco, marcas de gráfico. Não é cor de texto sobre fundo claro (2,6:1 sobre cal).
- **Terracotta Clay** (#c8651a): a argila. Fundo do painel de Bastidores, do muro de autores e do véu sobre capas. Em fundo claro, só para grafismo (3,6:1 sobre cal).
- **Terracotta Deep** (#9a4a0d): texto e botão em terracota sobre fundo claro (5,7:1 sobre cal; branco sobre ele dá 6,3:1).
- **Terracotta Ink** (#7a3a08): estado de hover de texto em terracota.
- **Peach** (#f4b07a) / **Peach Tint** (#fbe3cc): destaque de texto sobre fundo escuro (10,4:1 sobre dusk) e tons claros dos azulejos.

### Roxo
- **Ink Purple** (#552b7b): cor de Panorama e de marca secundária (9,4:1 sobre cal).
- **Ink Purple Deep** (#2a1640): fundo do painel de Ensaios.
- **Lilac** (#b9a3d6) / **Lilac Tint** (#e2d2f3) / **Rose** (#d98aa6): tons claros dos azulejos e do céu.

### Anoitecer (superfícies escuras)
- **Dusk** (#130a1b): fundo dos topos de página, das faixas escuras e do rodapé.
- **Dusk Raised** (#1c1027): faixa escura secundária.
- **Wall** (#24142f): o bloco da parede. Um degradê vertical sutil (de #2a1837 a #1d1028) e um fio claro no topo dão relevo.

### Cal (superfícies claras)
- **Cal** (#f6f2f8): fundo de página. Branco levemente violeta, nunca creme.
- **Cal Shade** (#ebe4f0): seção alternada.
- **Paper** (#ffffff): cartões e campos sobre cal.
- **Hairline** (#ddd3e5): bordas e divisores.

### Texto
- **Charcoal Ink** (#1a0f24): títulos.
- **Slate Ink** (#3a2a48): texto de leitura (11,8:1 sobre cal).
- **Mist Ink** (#6b5d76): texto de apoio e metadados (5,5:1 sobre cal).
- **Fog Ink** (#948aa0): só para elementos não essenciais, como texto de campo vazio. Não atinge AA sobre cal (3,0:1), então não serve para data, autor nem legenda.

### O céu
Degradê de fim de tarde em cinco paradas, de cima para baixo: #4b2c80, #8a58ad (30%), #d98aa6 (55%), #f6ab72 (78%), #e9772a.

### Named Rules
**The Sunset Wall Rule.** Toda abertura é preenchida pela luz do pôr do sol: o degradê do céu atravessa a parede da home com o sol atrás, a faixa de aberturas das seções e do arquivo, o friso do rodapé e as aberturas dos capítulos de série. O degradê corre contínuo por todas as aberturas de uma peça, em userSpaceOnUse, e nunca preenche um cartão, um botão ou um bloco inteiro.

**The Watercolor Rule.** A aquarela do projeto vive nas capas e ilustrações, e aparece pelo véu de um texto ou destaque. Ela não serve de fundo de abertura.

**The Readable Terracotta Rule.** Texto em terracota sobre fundo claro usa Terracotta Deep. Signal e Clay ficam para grafismo, onde 3:1 basta. Sobre fundo escuro vale o inverso: Signal e Peach são os tons legíveis.

**The Violet Neutral Rule.** Nenhum neutro é cinza puro nem preto puro. Texto, bordas e sombras têm matiz violeta.

## Section Palettes

Cada seção tem um painel de azulejo em duas cores, usado como capa da seção e como capa padrão de texto sem imagem. As formas alternam entre o tom A e o tom B em xadrez.

| Seção | Fundo | Tom A | Tom B | Cor do selo sobre cal |
|---|---|---|---|---|
| Bastidores | #c8651a | #fbe3cc | #f4b07a | forma #c8651a, texto #9a4a0d |
| Panorama | #552b7b | #e2d2f3 | #b9a3d6 | forma e texto #552b7b |
| Práticas | #f4b07a | #9a4a0d | #c8651a | forma #9a4a0d, texto #7a3a08 |
| Ensaios | #2a1640 | #b9a3d6 | #d98aa6 | forma e texto #2a1640 |

## Typography

**Títulos:** Bricolage Grotesque variável (eixos opsz 12–96, wght 200–800 e wdth 75–100), peso 700, entrelinha apertada e espaçamento levemente negativo. O eixo de tamanho óptico acompanha o corpo: títulos grandes ganham o corte de exibição, já bem apertado, então o espaçamento extra é pequeno (cerca de 1% do corpo). Ocupa o espaço como letreiro de fachada.
**Texto:** IBM Plex Sans, de 400 a 600.
**Apoio e dado:** IBM Plex Mono, em dois papéis. Nos textos de apoio grandes (a frase logo abaixo de um título, o subtítulo de um texto) e nos rótulos de dado (datas, contagens, legendas de eixo, o ano gravado no bloco). É a única família mono do site e substitui a Source Code Pro.

### Hierarchy
- **Display** (96px, entrelinha 0,93, espaçamento -3,6px): título do topo de página. Um por página.
- **Headline** (64px): título de destaque e de bloco grande.
- **Title** (44px): título de seção da página.
- **Card title** (24px): título de texto em cartão e em lista.
- **Lead** (17px, IBM Plex Mono, entrelinha 1,55, espaçamento -0,2px): frase de apoio abaixo de um título e subtítulo de texto. Em coluna de até 62 caracteres, porque a mono é mais larga.
- **Reading** (19px, entrelinha 1,65): corpo de um texto, em coluna de 720px.
- **Body** (16px, entrelinha 1,55): texto de interface.
- **Label** (13px, peso 600): selo de seção, filtro, botão pequeno.
- **Mono** (12px, IBM Plex Mono): data, contagem, legenda.

### Named Rules
**The Signboard Rule.** Só os títulos usam Bricolage. Nenhum parágrafo, rótulo ou botão usa a fonte de título.

**The Mono Lead Rule.** A mono aparece grande só como apoio de um título, nunca em sequência de parágrafos. O corpo de um texto e as descrições de cartão continuam em IBM Plex Sans.

**The Accent Phrase Rule.** O destaque de cor num título (Peach sobre escuro, Terracotta Deep sobre claro) é permitido uma vez por página, no trecho que carrega o sentido, como "sotaque brasileiro".

## Layout

Largura de conteúdo de 1200px, com coluna de leitura de 720px nos textos. Espaçamento em base 8px.

- **Topo escuro:** home, seções, autores, séries, arquivo, sobre, newsletter, escrever e 404 abrem com um topo em Dusk, com a navegação dentro dele.
- **Página de texto:** fundo claro do começo ao fim, para a leitura. A navegação fica sobre cal.
- **Alternância:** depois do topo, o conteúdo alterna cal e cal shade. Uma faixa escura pode voltar no meio da página para um bloco de destaque (autores, série, newsletter).

### A parede
- **Desktop:** 15 colunas de 80px na home. Em outras páginas a parede aparece menor: 25 colunas de 48px no arquivo, uma faixa de uma linha na seção.
- **Celular:** 8 colunas, com rolagem vertical. Nunca rolagem lateral, que esconde a maior parte do acervo.
- **Ordem:** sempre cronológica, da esquerda para a direita e de cima para baixo. O primeiro bloco de cada ano traz o ano gravado no canto.
- **Blocos fechados:** os dois últimos blocos ficam fechados, com contorno tracejado, à espera do próximo texto. O mesmo desenho marca capítulo de série ainda não publicado.

## Elevation & Depth

A profundidade é pequena e exata.

- **Aresta:** cada abertura tem espessura. A imagem de fundo é deslocada 3,5px para a direita e 4,5px para baixo, e a faixa que sobra mostra a aresta do bloco, mais clara de um lado.
- **Sombra:** cartões sobre cal usam sombra difusa em roxo (`rgba(42, 22, 64, .4)`), deslocada para baixo. Elementos sobre fundo escuro usam sombra preta translúcida.
- **Grão:** superfícies escuras recebem um grão fino em `soft-light`. É textura de reboco, quase imperceptível.

## Shapes

Cantos de 3px em blocos, cartões, botões e campos. 6px só em janela modal. Círculo perfeito para fotos de pessoas. Bordas de 1px em Hairline sobre claro e em branco a 12–16% sobre escuro.

## Components

### Parede
Grade de blocos com uma abertura por texto. Estados de uma abertura: acesa (padrão), apagada (fora do filtro ou da busca), em foco (contorno claro de 2,5px no bloco) e fechada (tracejado com um sinal de mais). Passar o mouse ou focar mostra título, seção, autor e data. Clicar abre o texto. Toda abertura é alcançável por teclado.

### Selo de seção
Forma de 18px seguida do nome da seção em Label. Cores na tabela de Section Palettes.

### Painel de azulejo
Padrão em xadrez das formas de uma seção. Usado no topo da página de seção, no cartão da seção em "Navegue pelo acervo" e como capa padrão.

### Muro de autores
Blocos em Terracotta Clay com abertura circular e a foto da pessoa por trás, com saturação reduzida a 70%. Blocos fechados no fim convidam quem ainda vai escrever.

### Véu
Faixa de blocos de argila na borda direita de uma capa em destaque. A imagem continua visível pelas aberturas.

### Friso
Fileira única de blocos de 48px, alternando as quatro formas, no topo do rodapé de todas as páginas. O degradê do pôr do sol corre na horizontal por todas as aberturas, de violeta a laranja, sobre o fundo dusk.

### Faixa de aberturas
Fileira (ou fileiras) de aberturas de 80 px, uma por texto, em ordem de publicação, no topo das páginas de seção e do arquivo. Mostram o degradê do pôr do sol, levam ao texto e crescem com mola ao passar o mouse. Rótulos de ano em Plex Mono no canto do primeiro texto de cada ano; o texto mais recente da seção leva moldura clara. No celular a faixa quebra em 8 colunas.

### Faixa de leitura
Fileira de aberturas de 24 px sob a navegação da página de texto, na forma da seção. Acende em Peach conforme a rolagem e fica fixa abaixo da navegação. Substitui a barra de progresso.

### Índice e ficha
Na página de texto, a coluna da esquerda lista os intertítulos, cada um com a forma da seção; o atual acende em Signal. A coluna da direita traz seção, série, temas e licença. Abaixo de 1240px o índice some e a ficha desce para depois do texto.

### Busca
Painel escuro (Dusk Raised) sobre o véu do site, com os resultados em Bricolage, a forma da seção em Peach e a data em Plex Mono.

### Topo escuro das páginas internas
Autores, séries, tags, arquivo, sobre, newsletter, escrever, contato, livros e 404 abrem com o mesmo topo: título gigante em Bricolage (última frase em Peach), texto de apoio em Plex Mono e uma peça de aberturas (muro de retratos, capítulos, faixa ou "404" aceso). As aberturas seguem a Sunset Wall Rule.

### Cartão de texto
Capa em 16:10 (imagem ou painel de azulejo), selo de seção, título em Card title, autor e data em Mist Ink.

### Botões
- **Primário:** fundo Terracotta Deep, texto branco, 46px de altura.
- **Sobre escuro:** fundo Terracotta Signal, texto Dusk.
- **Contorno:** fundo transparente, borda de 1px na cor do texto.
- **Foco:** contorno visível de 2px em Terracotta Signal, com 2px de afastamento.

### Capítulo de série
Bloco aberto para capítulo publicado: fundo Wall, número, título e uma abertura circular que mostra a ilustração do capítulo. Bloco fechado para capítulo futuro: tracejado, com título e "em breve".

### Barra de leitura
Na página de texto, uma faixa de aberturas de 24px sob a navegação. As aberturas acendem da esquerda para a direita conforme a leitura avança.

### Busca
Janela modal sobre a página escurecida. Resultados à esquerda, com o termo marcado no título. À direita, uma parede pequena em que só as aberturas encontradas ficam acesas.

## Motion

- **Um momento orquestrado por página.** Na home, as aberturas acendem em ordem cronológica no carregamento. Nenhum outro bloco anima sozinho ao entrar na tela.
- **Resposta a ações:** filtro, foco, hover e abertura de modal animam em 150 a 250ms, com curva de desaceleração (`cubic-bezier(0.23, 1, 0.32, 1)`).
- **Um movimento contínuo, no máximo:** a luz por trás da parede da home pode variar de intensidade bem devagar.
- **Menos movimento:** com `prefers-reduced-motion`, tudo aparece no estado final e o movimento contínuo é desligado.
- **Troca automática:** qualquer coisa que avance sozinha mostra o progresso e pausa com hover, foco ou toque.

## Do's and Don'ts

### Do:
- **Do** indicar a seção pela forma em todo lugar — **The Shape First Rule**.
- **Do** preencher as aberturas com o degradê do céu, de forma contínua pela peça inteira — **The Sunset Wall Rule**.
- **Do** guardar a aquarela para capas e ilustrações, vista pelo véu — **The Watercolor Rule**.
- **Do** usar Terracotta Deep para texto em terracota sobre claro — **The Readable Terracotta Rule**.
- **Do** usar Mist Ink para datas, autores e legendas.
- **Do** manter a parede em ordem cronológica e em 8 colunas no celular.
- **Do** preservar o conteúdo dos textos migrados do Medium como registro histórico. Mudanças são de exibição, nunca de conteúdo.

### Don't:
- **Don't** preencher cartão, botão ou bloco com degradê.
- **Don't** usar Terracotta Signal, Terracotta Clay ou Fog Ink como cor de texto sobre fundo claro.
- **Don't** redesenhar as quatro formas nem criar uma quinta sem criar uma seção.
- **Don't** usar Bricolage em parágrafo, rótulo ou botão.
- **Don't** animar a entrada de cada bloco ao rolar a página.
- **Don't** usar creme como fundo claro nem cinza ou preto puros.
- **Don't** usar o cobogó como textura decorativa de fundo. Cada bloco na tela representa um texto, uma pessoa ou uma seção.
