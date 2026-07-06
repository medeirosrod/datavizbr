// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://datavizbr.com.br',
  image: {
    service: {
      entrypoint: 'astro/assets/services/noop'
    }
  }
});