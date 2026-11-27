// Gera no build um JPEG 1200x630 por texto com capa. Usa o sharp direto porque o serviço de
// imagem do Astro não amplia capas pequenas nem completa as sobras, e o tamanho aqui é fixo.
import type { APIRoute, GetStaticPaths } from 'astro';
import sharp from 'sharp';
import { getPosts } from '../../lib/data';
import { capaOg, OG_ALTURA, OG_LARGURA } from '../../lib/og';

export const getStaticPaths = (async () =>
  (await getPosts()).flatMap((post) => {
    const capa = capaOg(post);
    return capa ? [{ params: { slug: post.id }, props: { capa } }] : [];
  })) satisfies GetStaticPaths;

export const GET: APIRoute<{ capa: NonNullable<ReturnType<typeof capaOg>> }> = async ({ props: { capa } }) => {
  // `fsPath` é o caminho do arquivo original; o Astro o define, mas não o declara no tipo.
  const { fsPath } = capa.imagem as typeof capa.imagem & { fsPath?: string };
  if (!fsPath) throw new Error(`Capa sem caminho de arquivo: ${capa.url}`);

  const jpeg = await sharp(fsPath) // em GIF, só o primeiro quadro
    .rotate() // orientação do EXIF
    .flatten({ background: '#ffffff' }) // transparência vira papel branco
    .resize(OG_LARGURA, OG_ALTURA, { fit: capa.ajuste, background: '#130a1b' }) // faixas em Dusk
    .jpeg({ quality: 85, mozjpeg: true })
    .toBuffer();

  return new Response(new Uint8Array(jpeg), { headers: { 'Content-Type': 'image/jpeg' } });
};
