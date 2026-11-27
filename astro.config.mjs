// @ts-check
import { defineConfig, sharpImageService } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://datavizbr.com.br',
  integrations: [mdx()],
  redirects: { '/nordeste': '/series/nordeste-em-dados' },
  image: {
    // Dois GIFs migrados do Medium somam 421 e 281 milhões de pixels (todos os quadros),
    // acima do limite padrão do sharp (268 milhões).
    service: sharpImageService({ limitInputPixels: 500_000_000 })
  }
});