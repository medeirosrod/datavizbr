// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://datavizbr.com.br',
  integrations: [mdx()],
  redirects: { '/nordeste': '/series/nordeste-em-dados' },
  image: {
    service: {
      entrypoint: 'astro/assets/services/noop'
    }
  }
});