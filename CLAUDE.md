# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**datavizbr** is a blog platform for data visualization content built with Astro. It features 70+ posts migrated from Medium, organized by sections (Panorama, Práticas, Bastidores, Ensaios), with support for authors, series, tags, and related content.

## Quick Commands

```bash
npm install          # Install dependencies
npm run dev          # Start dev server (http://localhost:4323)
npm run build        # Build for production
npm run preview      # Preview production build locally
npm run astro -- <cmd>  # Run any Astro CLI command
```

## Architecture Overview

### Content Structure
- **Posts** (`src/content/posts/`): Markdown files with frontmatter (title, author, date, section, tags, cover image)
- **Authors** (`src/content/autores/`): Author metadata with bios, roles, and profile photos
- **Collections**: Managed via Astro Content Collections API (`getCollection()`)
- **Assets**: Blog post images in `src/assets/blog/<post-slug>/`, author photos in `src/content/autores/_fotos/`

### Key Frontmatter Fields
Posts use:
- `titulo`, `autores[]`, `publicado_em`, `secao` (panorama|praticas|bastidores|ensaios)
- `tags[]` (22 standard tags: Dataviz, Dados, Design, COVID-19, Acessibilidade, etc)
- `capa` (cover image path for thumbnails)
- `medium_url_original` (source URL from Medium migration)
- `arquivo` (true = published but archived; filters affect tag pages/lists)

### Page Structure
- **Sections** (`src/pages/<secao>.astro`): Filter posts by section with pagination
- **Tags** (`src/pages/tags/index.astro` & `[slug].astro`): Dynamic tag pages; note: `[slug].astro` has explicit filter on line 22 for posts
- **Authors** (`src/pages/autores.astro` & `autores/[slug].astro`): Author profiles and their posts
- **Series** (`src/pages/series.astro` & `series/[id].astro`): Grouped post collections
- **Post Detail** (`src/pages/posts/[id].astro`): Individual post rendering with layout

### Layout System
- `BaseLayout.astro`: Global layout (header, footer, nav)
- `PostLayout.astro`: Post-specific layout (date, author info, related posts)

### Key Components
- `AutorNome.astro`: Renders author name/link from author ID
- `FormattedDate.astro`: Formats dates in pt-BR locale
- `HeaderLink.astro`: Navigation link component
- `Header.astro` / `Footer.astro`: Site chrome

## Recent Changes & Context

**Medium Migration (Latest):**
- 70 posts extracted from Medium blog
- 100+ images per post inserted into markdown bodies (correct file paths, alt text)
- 62 posts tagged with 22 standard tags
- 24 author photos extracted from Medium (512x512px)
- Duplicate cover images removed from post bodies (covers kept in frontmatter for thumbnails)
- Archived posts (`arquivo: true`) now included in tag pages (filter removed from `[slug].astro`)
- Build optimized: image processing disabled to handle large GIFs (Astro config uses noop service)

**Known State:**
- All posts build successfully (134 pages)
- Posts with `rascunho: true` are hidden (excluded from collections)
- Posts with `arquivo: true` are visible but marked as archive (controlled by `!data.rascunho` filter)
- Tags page filters posts correctly; individual tag pages show ~50 posts per tag

## Common Development Patterns

### Adding/Editing Posts
1. Create `.md` file in `src/content/posts/`
2. Include all required frontmatter fields
3. Reference images as `![alt](../../assets/blog/<slug>/<image>)`
4. Run `npm run build` to validate; check for `ImageNotFound` errors (path mismatches)

### Working with Tags
- Standard tags live in post frontmatter (array)
- Tag pages auto-generate from posts; no manual page creation needed
- Filtering: both `index.astro` and `[slug].astro` must match on `!data.rascunho` filter

### Image Handling
- Cover images in frontmatter used for thumbnails (not displayed in post body)
- Post body images must exist in `src/assets/blog/<post-slug>/`
- If image resolution causes Astro optimization errors, disable in `astro.config.mjs` (currently disabled for large GIFs)

## File Locations to Know

- `src/consts.ts`: Site-wide constants (sections, site URL)
- `src/content/config.ts`: Content collection schemas
- `astro.config.mjs`: Build/image optimization settings
- `tsconfig.json`: TypeScript config (strict mode)
- `src/styles/`: Global CSS variables (--space-*, --color-*, --fs-*, etc)

## Notes on Image Optimization

Currently disabled (`noop` service in `astro.config.mjs`) due to large GIF files (some >3MB) exceeding Sharp pixel limits. If re-enabling, compress GIFs or convert to WebP first.

