---
name: datavizbr
description: Visualização de dados com sotaque brasileiro
colors:
  terracotta-signal: "#e67e2c"
  terracotta-hover: "#c8651a"
  terracotta-deep: "#9a4a0d"
  terracotta-tint: "#fce8d6"
  terracotta-soft: "#fef5ec"
  ink-purple: "#552b7b"
  ink-purple-hover: "#3f1f5d"
  ink-purple-deep: "#2a1640"
  purple-tint: "#ead8f7"
  charcoal-ink: "#1a0f24"
  slate-ink: "#3a2a48"
  mist-ink: "#6b5d76"
  fog-ink: "#948aa0"
  hairline: "#e8e3ee"
  hairline-strong: "#d2c9dd"
  paper: "#ffffff"
  paper-soft: "#faf8fc"
  signal-success: "#15be53"
  signal-error: "#c83838"
  acervo-bastidores-bg: "#1f1028"
  acervo-panorama-bg: "#1a1030"
  acervo-praticas-bg: "#1a1528"
  acervo-ensaios-bg: "#0e0a18"
typography:
  display:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "56px"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-1.6px"
  headline:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "44px"
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: "-1.0px"
  title:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.6px"
  body:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.60
  label:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 600
    letterSpacing: "0.8px"
  mono:
    fontFamily: "Source Code Pro, SFMono-Regular, ui-monospace, Menlo, monospace"
    fontSize: "13px"
    fontWeight: 500
    lineHeight: 1.70
  numeral:
    fontFamily: "Source Code Pro, SFMono-Regular, ui-monospace, Menlo, monospace"
    fontSize: "2.8rem"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.04em"
rounded:
  micro: "1px"
  standard: "4px"
  comfortable: "5px"
  relaxed: "6px"
  large: "8px"
  pill: "999px"
spacing:
  space-4: "8px"
  space-8: "16px"
  space-12: "24px"
  space-16: "32px"
  space-24: "48px"
  space-32: "64px"
components:
  button-primary:
    backgroundColor: "{colors.terracotta-deep}"
    textColor: "#ffffff"
    rounded: "{rounded.standard}"
    padding: "10px 20px"
  button-primary-hover:
    backgroundColor: "{colors.terracotta-deep}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.terracotta-deep}"
    rounded: "{rounded.standard}"
    padding: "10px 20px"
  button-quiet:
    backgroundColor: "transparent"
    textColor: "{colors.mist-ink}"
    rounded: "{rounded.standard}"
    padding: "10px 20px"
  card:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.relaxed}"
  badge-primary:
    backgroundColor: "{colors.terracotta-tint}"
    textColor: "{colors.terracotta-deep}"
    rounded: "{rounded.standard}"
  tag:
    backgroundColor: "{colors.paper-soft}"
    textColor: "{colors.mist-ink}"
    rounded: "{rounded.standard}"
---

# Design System: datavizbr

## Overview

**Creative North Star: "O Caderno de Campo"**

datavizbr é o caderno de campo de quem estuda e produz visualização de dados no Brasil desde 2007 — não uma vitrine de agência, não um blog corporativo. O laranja funciona como marca-texto: o gesto de destacar uma ideia importante no meio da leitura. O roxo profundo funciona como tinta de anotação: a camada mais analítica, presente em títulos de seção e no rodapé, onde o site assume um tom mais denso e reflexivo. A tipografia técnica (IBM Plex Sans para texto, Source Code Pro para código) reforça que este é um instrumento de trabalho de quem lida com dados todos os dias, não uma peça de marketing.

O sistema é editorial antes de ser "de produto": hierarquia tipográfica forte, pouca decoração, cor usada com intenção e não como preenchimento. Este não é o visual de um SaaS genérico — sem gradiente roxo-azul, sem cards aninhados dentro de cards, sem ícone em tile arredondado acima de cada título. Também não é um blog corporativo frio: a voz autoral e a presença do laranja como acento vivo mantêm a personalidade humana do curador em primeiro plano.

**Key Characteristics:**
- Contraste quente-frio deliberado: laranja quente para ação e destaque, roxo frio e profundo para densidade analítica.
- Tipografia técnica (IBM Plex Sans/Mono) tratada como interface de trabalho, não como enfeite editorial.
- Componentes precisos e discretos — bordas finas, sombras ambiente, raios de canto pequenos.
- Cor usada com intenção: o laranja aparece em pontos de decisão (links, CTAs, ativo), nunca como fundo decorativo generalizado.

## Colors

Paleta quente e intelectual: laranja terroso como energia e chamada à ação, roxo profundo como camada analítica e de marca, neutros de base violeta (não cinza puro) para texto e fundo.

### Primary
- **Terracotta Signal** (#e67e2c): cor de marca e ação — estado ativo de navegação, foco de seção "Bastidores", focus ring, linhas de gráfico. Usada como o marca-texto do sistema: pontual, nunca como fundo de área grande, e nunca como cor de texto (links inclusive — ver The Readable Terracotta Rule).
- **Terracotta Hover** (#c8651a): estado de hover/pressed de elementos gráficos em Terracotta Signal (ex.: links).
- **Terracotta Deep** (#9a4a0d): texto e fundos de botão que carregam a identidade terracota mas precisam de contraste AA — eyebrow labels, texto de badge, fundo do botão primário.
- **Terracotta Tint** (#fce8d6) / **Terracotta Soft** (#fef5ec): fundos suaves para badges e realces sutis em tom laranja.

### Secondary
- **Ink Purple** (#552b7b): cor de marca secundária — seção "Panorama", tema alternativo do site, footer (como fundo escuro `[data-theme="roxo-dark"]`). É a camada intelectual/densa do sistema.
- **Ink Purple Hover** (#3f1f5d) / **Ink Purple Deep** (#2a1640): estados de hover e fundo mais escuro (footer).
- **Purple Tint** (#ead8f7): fundo suave para badges em tom roxo (seção "Panorama", séries).

### Neutral
- **Charcoal Ink** (#1a0f24): cor de título/heading — não é preto puro, tem matiz violeta.
- **Slate Ink** (#3a2a48): texto de label/UI secundária.
- **Mist Ink** (#6b5d76): cor de corpo de texto padrão.
- **Fog Ink** (#948aa0): metadados, datas, legendas discretas.
- **Hairline** (#e8e3ee) / **Hairline Strong** (#d2c9dd): bordas e divisores.
- **Paper** (#ffffff) / **Paper Soft** (#faf8fc): fundo de página e fundo levemente destacado (cards secundários, seções alternadas).

### Surfaces escuras do Acervo
- **Acervo Bastidores BG** (#1f1028) / **Acervo Panorama BG** (#1a1030) / **Acervo Práticas BG** (#1a1528) / **Acervo Ensaios BG** (#0e0a18): fundos escuros bespoke da seção "Navegue pelo acervo" — uma variação tonal roxa/violeta por seção editorial, mais escura que qualquer neutro do resto do sistema. Uso exclusivo dessa seção; não reutilizar como fundo de card comum.

### Named Rules
**The Marker Rule.** Terracotta Signal é usado como marca-texto, não como preenchimento: aparece em estados ativos, focus ring e acentos gráficos pontuais, nunca como fundo de blocos grandes de conteúdo nem como cor de texto de link (ver The Readable Terracotta Rule).

**The Readable Terracotta Rule.** Terracotta Signal (#e67e2c) sozinho não atinge 4.5:1 sobre branco — reservado a usos gráficos/decorativos (linhas de gráfico, sublinhados, focus ring, ícones grandes) onde 3:1 basta. Qualquer texto ou botão que carregue significado — incluindo links de texto corrido (`--fg-link` no tema padrão) — usa **Terracotta Deep** (#9a4a0d, ~6.25:1) em vez do tom vivo. Exceção: nos temas escuros (`roxo-dark`), o laranja vivo é o que atinge contraste suficiente sobre o fundo roxo escuro — não trocar por Terracotta Deep ali.

## Typography

**Display/Body Font:** IBM Plex Sans (com fallback -apple-system, BlinkMacSystemFont, system-ui, sans-serif)
**Mono/Code Font:** Source Code Pro (com fallback SFMono-Regular, ui-monospace, Menlo, monospace)

**Character:** Uma sans técnica e neutra com toque editorial — pesos fortes (700) em títulos com tracking negativo dão presença sem recorrer a serifas; o mono aparece só onde o conteúdo é literalmente código ou dado tabular.

### Hierarchy
- **Display** (700, 56px, lh 1.05, ls -1.6px): hero da home, usada raramente — no máximo um título por página.
- **Headline** (700, 44px, lh 1.10, ls -1.0px): título principal de post/página (`h1`).
- **Title** (700, 32px, lh 1.15, ls -0.6px): título de seção dentro da página (`h2`).
- **Sub-title** (700, 24px, lh 1.20, ls -0.3px): título de card/bloco (`h3`).
- **Body** (400, 16px, lh 1.60): texto corrido; largura de leitura confortável em `--content-width: 720px`.
- **Body Large** (400, 19px, lh 1.55): lead/chapada de abertura de post.
- **Label/Eyebrow** (600, 12px, ls 0.8px, uppercase, cor Terracotta Deep): rótulo de categoria/seção acima de títulos.
- **Caption/Micro** (500, 13px/11px): metadados — data, autor, tempo de leitura.
- **Numeral** (700, 2.8rem, lh 1, ls -0.04em, mono): numerais gigantes de contagem por seção na "Navegue pelo acervo" — único uso desse tamanho no sistema, reservado a esse papel de "índice/contador editorial".

### Named Rules
**The Tabular Numbers Rule.** Números que aparecem lado a lado ou em sequência (datas, contadores) usam `font-feature-settings: "tnum"` (classe `.t-tnum`) para não desalinhar visualmente.

## Layout

Grade de largura única, sem sistema de colunas: `--max-width: 1080px` para o layout geral, `--content-width: 720px` para o corpo de texto de um post (largura de leitura confortável), padding lateral de `--padding-x: 32px`. Espaçamento em base 8px (`--space-4` a `--space-48`). Nav é `sticky` no topo com fundo translúcido (`backdrop-filter: blur(12px)`); abaixo de 768px, a navegação principal colapsa em overlay full-screen (`.nav-mobile`) acionado por um botão hambúrguer animado em três barras.

## Elevation & Depth

O sistema usa sombras ambiente e discretas, nunca estruturais: profundidade é sinal de "isto é uma superfície separada", não de hierarquia de importância. Todas as sombras usam a cor de marca roxa como base (`rgba(85, 43, 123, ...)`), o que dá um tom mais quente e integrado do que sombras cinza neutras.

### Shadow Vocabulary
- **elev-1** (`0 2px 6px rgba(85,43,123,0.06)`): elevação mínima — cards em listas, badges.
- **elev-2** (`0 12px 28px rgba(85,43,123,0.08)`): elevação padrão de `.card`.
- **elev-3** (dupla sombra difusa): `.card-elevated` — destaque editorial, ex. card em carrossel "Em destaque".
- **elev-4**: elevação máxima, reservada a overlays/modais (busca).
- **focus-ring** (`0 0 0 3px rgba(230,126,44,0.25)`): anel de foco em laranja translúcido, usado em `.btn`, `.input`.

### Named Rules
**The Purple Ambient Rule.** Toda sombra do sistema nasce da cor de marca roxa, nunca de preto puro — mesmo em elementos com tema laranja.

## Shapes

Cantos discretos e consistentes: `--radius-standard: 4px` para botões, badges, inputs e tags; `--radius-relaxed: 6px` para cards; `--radius-pill: 999px` reservado a elementos circulares/pill explícitos (não é o padrão de botão). Bordas finas de 1px em `--border-default` definem a maior parte dos contornos; a única borda grossa do sistema é o acento de citação (`blockquote`, 3px sólido em Terracotta Signal), reservada para esse único uso editorial.

## Components

### Buttons
- **Shape:** `--radius-standard` (4px), padding `--space-5 --space-10` (padrão), `--space-3 --space-7` (`.btn-sm`), `--space-7 --space-12` (`.btn-lg`).
- **Primary:** fundo Terracotta Deep, texto branco (~6.25:1, AA); hover escurece via `filter: brightness(0.85)`.
- **Ghost:** fundo transparente, texto Terracotta Deep, borda Terracotta Signal; hover preenche com Terracotta Soft.
- **Quiet:** fundo transparente, texto Slate/Label, borda Hairline; hover escurece borda e texto para Heading.
- **Focus:** anel laranja translúcido (`--focus-ring`), sem outline padrão do navegador.

### Badges
- **Estilo:** pill discreto, fundo tinta clara da cor correspondente, texto na versão "deep" da mesma cor, `--radius-standard`.
- **Por seção editorial:** cada seção (Bastidores, Panorama, Práticas, Ensaios) tem sua própria combinação de badge, derivada da paleta de marca — nunca uma cor arbitrária fora do sistema.
- **Estado especial:** `.badge-arquivo` usa itálico + neutro para sinalizar conteúdo histórico sem tratá-lo como erro ou aviso.

### Cards / Containers
- **Corner Style:** `--radius-relaxed` (6px).
- **Background:** Paper (#ffffff).
- **Shadow Strategy:** `elev-2` padrão, `elev-3` (`.card-elevated`) para destaque editorial pontual.
- **Border:** 1px Hairline.

### Inputs / Fields
- **Style:** fundo Paper, borda Hairline, `--radius-standard`, padding `--space-5 --space-7`.
- **Focus:** borda muda para cor de marca (`--border-focus`) + `--focus-ring`.

### Navigation
- **Style:** links com sublinhado animado (`::after`, `scaleX` da direita para a esquerda no hover/active) em vez de fundo ou pill — mantém a nav limpa e tipográfica.
- **Estado ativo/hover:** cor muda para Terracotta Signal.
- **Mobile:** colapsa em overlay full-screen com links grandes (19px) empilhados verticalmente.

### Tags
- **Style:** fundo Paper Soft, borda Hairline, texto Mist Ink; hover preenche com Terracotta Soft e muda texto/borda para tons de marca.

### Curador (assinatura autoral na home)
- **Estrutura:** foto circular (72px, `object-fit: cover`) + bio curta em terceira pessoa + link "Conheça o projeto →", separados do restante da seção por uma linha divisória (`border-bottom: 1px solid var(--border-default)`).
- **Propósito:** dar rosto e nome ao curador do datavizbr logo na segunda dobra da home, sem precisar de uma seção "sobre" completa. Abaixo dele, uma legenda curta ("Recomendados pela curadoria para começar por aqui.") introduz os posts escolhidos a dedo em tom impessoal/comunidade, mantendo a curadoria pessoal implícita sem usar primeira pessoa.
- **Mobile:** foto e texto empilham verticalmente abaixo de 640px.

### Curador em Destaque (página Sobre)
- **Estrutura:** variante maior do componente Curador — foto circular de 120px (vs. 72px na home), nome como link direto para a página do autor (`/autores/{id}`) em heading (`--fs-h3`), bio completa (`quem_e`) abaixo. Fica logo após o `<h1>` da página, antes de qualquer parágrafo narrativo.
- **Propósito:** a página "Sobre" é o único lugar do site cujo trabalho é provar que existe uma pessoa real e credível por trás do projeto — por isso usa a versão mais destacada do componente, e a posiciona no topo em vez de no fim, garantindo que a identidade não dependa de o leitor rolar a página inteira.
- **Mobile:** foto e texto empilham verticalmente abaixo de 600px.

## Do's and Don'ts

### Do:
- **Do** usar Terracotta Signal como acento gráfico pontual (focus ring, estado ativo, linhas de gráfico) — **The Marker Rule**.
- **Do** usar Terracotta Deep para links e qualquer texto em terracota no tema padrão — **The Readable Terracotta Rule**.
- **Do** basear toda sombra em roxo translúcido, nunca em preto puro — **The Purple Ambient Rule**.
- **Do** manter badges de seção fiéis à cor de marca daquela seção (Bastidores/Panorama = laranja/roxo, Práticas/Ensaios = tons neutros de roxo).
- **Do** preservar o conteúdo dos 70+ posts migrados do Medium como registro histórico — mudanças aqui são de formatação/exibição, nunca de conteúdo.

### Don't:
- **Don't** introduzir gradiente roxo-azul, cards aninhados dentro de cards, ou ícone em tile arredondado acima de título — os tiques visuais típicos de UI genérica gerada por IA que este sistema deliberadamente evita.
- **Don't** usar preto ou cinza neutro puro em texto ou sombra — todos os neutros do sistema têm matiz violeta.
- **Don't** aplicar `--radius-pill` a botões padrão; pill é reservado a elementos explicitamente circulares.
- **Don't** dar à borda-acento do blockquote (3px sólido) um uso genérico em cards — é um gesto editorial único, não um padrão reutilizável de "destaque".
