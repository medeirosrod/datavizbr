# Planejamento — datavizbr

Auditoria completa de páginas, rotas e componentes em 18/jun/2026.

## Rotas existentes (todas mapeadas)

| Rota | Arquivo | Estado |
|---|---|---|
| `/` | `src/pages/index.astro` | OK |
| `/404` | `src/pages/404.astro` | OK |
| `/arquivo` | `src/pages/arquivo.astro` | OK |
| `/bastidores` | `src/pages/bastidores.astro` | OK |
| `/panorama` | `src/pages/panorama.astro` | OK |
| `/praticas` | `src/pages/praticas.astro` | OK |
| `/ensaios` | `src/pages/ensaios.astro` | OK |
| `/posts/[...slug]` | `src/pages/posts/[...slug].astro` | OK |
| `/autores` | `src/pages/autores.astro` | OK |
| `/autores/[id]` | `src/pages/autores/[id].astro` | OK |
| `/series` | `src/pages/series.astro` | OK |
| `/series/[id]` | `src/pages/series/[id].astro` | OK |
| `/livros` | `src/pages/livros.astro` | OK |
| `/livros/[slug]` | `src/pages/livros/[slug].astro` | OK |
| `/tags` | `src/pages/tags/index.astro` | OK |
| `/tags/[slug]` | `src/pages/tags/[slug].astro` | OK |
| `/newsletter` | `src/pages/newsletter.astro` | OK |
| `/rss.xml` | `src/pages/rss.xml.js` | OK |
| `/sobre` | `src/pages/sobre/index.astro` | OK |
| `/sobre/contato` | `src/pages/sobre/contato.astro` | OK |
| `/sobre/escrever` | `src/pages/sobre/escrever.astro` | OK |

Todas as rotas do menu (`NAV_PRINCIPAL`, `NAV_RODAPE`) existem. **Nenhuma página está faltando.**

---

## Bugs encontrados

### P1 — Afeta rendimento visual ou quebra layout

1. **`--radius-pill` não definido** (`src/styles/tokens.css`)
   Usado em 3 lugares mas a variável não existe: `series.astro:280`, `tags/index.astro:83`, `livros/[slug].astro:232`. Elementos perdem border-radius.
   **Fix:** Adicionar `--radius-pill: 999px;` em `tokens.css`.

2. **Template syntax quebrada em classe dinâmica** (`src/pages/livros.astro:38`)
   ```astro
   <span class="livro-acesso livro-acesso-{livro.data.tipo_acesso}">
   ```
   `{}` dentro de `class=""` não funciona em Astro. Deveria ser `class:list`.
   **Fix:** Usar `class:list={['livro-acesso', `livro-acesso-${livro.data.tipo_acesso}`]}`.

### P2 — Lógica incorreta, sem quebra visível

3. **Condição de redes sociais frágil** (`src/pages/autores.astro:46`)
   ```astro
   {autor.data.redes || (autor.data.twitter || ...) && (...)}
   ```
   `autor.data.redes` não existe no schema — a condição funciona por acaso via curto-circuito, mas é enganosa.
   **Fix:** Remover `autor.data.redes ||`.

### P3 — Placeholder / não funcional

4. **Newsletter form não submete** (home + `/newsletter`)
   `onsubmit="return false;"` — não há integração com serviço de email.
   **Decisão necessária:** Integrar com serviço (ConvertKit, Mailchimp, Buttondown) ou manter como placeholder.

5. **HeroChart usa dados estáticos** (`src/components/HeroChart.astro:142`)
   `window.chartData || [dados fixos até 2025]` — ignorando dados reais do acervo.
   **Fix:** Passar contagens reais de posts/autores por ano via frontmatter do Astro.

---

## Melhorias estruturais

6. **Duplicação massiva nas páginas de seção**
   `bastidores.astro`, `panorama.astro`, `praticas.astro`, `ensaios.astro` são 95% idênticos (mesma query, grid, estilo), diferindo apenas em título, descrição e cor do placeholder.
   **Sugestão:** Extrair para `src/pages/secao/[slug].astro` com `getStaticPaths` dinâmico, ou criar componente `SecaoLayout`.

7. **Inconsistência visual nos cards de série**
   `series.astro` posiciona badge "Parte N" em `top left` com fundo escuro; `series/[id].astro` posiciona em `top right` com cor primária. Deviam seguir o mesmo padrão.

8. **`[...slug].astro` usa `any` no tipo do post**
   `interface Props { post: any; }` — quebra a segurança de tipos.
   **Fix:** Importar `CollectionEntry<'posts'>`.

---

## Prioridade sugerida

| # | Tarefa | Impacto | Esforço |
|---|---|---|---|
| 1 | Adicionar `--radius-pill` | 🐛 Bug visual | 5min |
| 2 | Consertar classe dinâmica em `livros.astro` | 🐛 Bug de render | 5min |
| 3 | Limpar condição de redes em `autores.astro` | 🧹 Cleanup | 5min |
| 4 | Integrar newsletter com serviço real | ✨ Feature | médio |
| 5 | HeroChart com dados reais | ✨ Feature | médio |
| 6 | Refatorar seções para rota dinâmica | 🏗️ Estrutural | grande |
| 7 | Padronizar cards de série | 🎨 UI | pequeno |
| 8 | Tipar `post` em `[...slug].astro` | 🧹 Cleanup | 5min |
