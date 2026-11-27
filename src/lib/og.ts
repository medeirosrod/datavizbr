// Imagem de compartilhamento (Open Graph e Twitter): tamanho e escolha da capa de cada texto.
import type { CollectionEntry } from 'astro:content';

export const OG_LARGURA = 1200;
export const OG_ALTURA = 630;

/**
 * Capa que vira a imagem de compartilhamento do texto; `undefined` quando não há capa
 * (o BaseLayout usa então a og-default.png).
 *
 * A `capa_destaque` é desenhada para formato largo, então preenche o quadro com corte central
 * (`cover`). A `capa` tem proporção livre (retratos, gráficos, cartazes), então entra inteira,
 * com faixas nas sobras (`contain`).
 */
export function capaOg({ id, data }: CollectionEntry<'posts'>) {
  const imagem = data.capa_destaque ?? data.capa;
  if (!imagem) return undefined;
  return {
    url: `/og/${id}.jpg`,
    imagem,
    alt: (data.capa_destaque ? data.capa_destaque_alt : data.capa_alt) || `Capa do texto “${data.titulo}”`,
    ajuste: data.capa_destaque ? ('cover' as const) : ('contain' as const),
  };
}
