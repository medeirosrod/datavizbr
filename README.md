# Datavizbr: versão opensource

```sh
npm create astro@latest -- --template blog
```

Funções:

- ✅ Estelização mínima (faça do seu jeito!)
- ✅ 100/100 em perfomance Lighthouse
- ✅ SEO-friendly com URLs canonical e dados Open Graph
- ✅ Suporte a Sitemap
- ✅ Suporte a RSS Feed
- ✅ Suporte a Markdown & MDX

## 🚀 Estrutura do projeto

Dentro do projeto Astro, você verá essas pastas e arquivos:

```text
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   ├── content/
│   ├── layouts/
│   └── pages/
├── astro.config.mjs
├── README.md
├── package.json
└── tsconfig.json
```

Astro procura por arquivos `.astro` ou `.md` dentro do diretório `src/pages/`. Cada página é exposta a essa rota baseada no nome do arquivo.

O diretório `src/content/` contem as coleções dos Markdown e documentos MDX relacionados. Qualquer artefato como imagens deve ser colocado na pasta `public/`.

Veja a [documentação do Astro](https://docs.astro.build).

## Credit

Esse tema é baseado no [Bear Blog](https://github.com/HermanMartinus/bearblog/).