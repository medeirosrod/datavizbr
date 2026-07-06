# datavizbr — repo guide

## Stack
- **Astro 6** + TypeScript (strict), MDX, static site
- Node >=22.12.0, npm

## Commands
| `npm run dev`      | dev server at `localhost:4321` |
| `npm run build`    | static site to `dist/`         |
| `npm run preview`  | preview built site             |
| `npm run astro check` | type-check via `@astrojs/check` |

There is no lint, format, or test setup.

## Content architecture (all in Portuguese)

Four collections defined in `src/content.config.ts` — posts, autores, series, livros. Markdown with YAML frontmatter.

| Directory | Key fields |
|---|---|
| `src/content/posts/` | `autores` (ref array), `secao`, `publicado_em`, `tags`, `destaque`, `rascunho`, `arquivo`, `serie` (ref) |
| `src/content/autores/` | `nome`, `papel` (curadoria/recorrente/convidado), `ativo` |
| `src/content/series/` | `titulo`, `status`, `iniciada_em` |
| `src/content/livros/` | `organizadores` (ref array), `ano`, `tipo_acesso` |

### Draft & archive flags
- `rascunho: true` = draft — hidden in production (`import.meta.env.PROD`), excluded from `getStaticPaths`
- `arquivo: true` = migrated from Medium — hidden from RSS feed but visible on site
- To publish a draft, set `rascunho: false` (or remove it)

### Editorial sections (`secao`)
`bastidores` | `panorama` | `praticas` | `ensaios` — defined in `src/content/config/secoes.json` and `src/consts.ts`

### Author IDs
Slugs from author name: `rodrigo-medeiros`, `tatyana-mendes`, etc. Referenced as `autores: [id]` in post frontmatter. The `converte_posts.py` script maps real names to slugs.

## Key paths
- `src/consts.ts` — site name, tagline, navigation links, social URLs
- `src/lib/data.ts` — `getPosts()`, `getAutores()`, `getSeries()`, `getLivros()` + filtered queries
- `src/layouts/BaseLayout.astro` — main layout with nav, footer, SEO/meta
- `src/layouts/PostLayout.astro` — post layout with prev/next nav
- `src/pages/posts/[...slug].astro` — dynamic post route (pre-renders via `getStaticPaths`)
- `src/styles/global.css` → `tokens.css` (design tokens), `base.css` (reset), `animations.css`
- `src/scripts/animations.js` — GSAP + D3 animations on homepage

## CDN dependencies (homepage only, `is:inline`)
- GSAP 3.12.5 + ScrollTrigger
- D3.js 7.8.5

## Custom scripts (Python, root directory)
- `converte_posts.py entrada/ saida/` — converts Medium-flavored .md to blog format (YAML frontmatter, auto-slug, section classification, author ID mapping)
- `cria_autores.py` — scaffold author .md files with basic frontmatter

## Deployment
Static site (no SSR). Output goes to `dist/`. Live at `https://datavizbr.com.br`.

## Dev server
- Astro dev server on port **4321**
- `.astro/` is generated types (gitignored)
- Generated types live at `.astro/types.d.ts`
