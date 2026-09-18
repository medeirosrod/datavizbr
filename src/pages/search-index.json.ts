// src/pages/search-index.json.ts
import type { APIRoute } from 'astro';
import { getPosts, getAutores, stripMarkdown } from '../lib/data';
import { getSecaoLabel } from '../consts';

export const prerender = true;

export const GET: APIRoute = async () => {
  const [posts, autores] = await Promise.all([getPosts(), getAutores()]);
  const autoresPorId = new Map(autores.map((a) => [a.id, a.data.nome]));

  const documentos = posts.map((post) => {
    const nomesAutores = post.data.autores
      .map((ref) => autoresPorId.get(ref.id))
      .filter((nome): nome is string => Boolean(nome));

    return {
      id: post.id,
      titulo: post.data.titulo,
      subtitulo: post.data.subtitulo ?? '',
      descricao: post.data.descricao ?? '',
      tags: post.data.tags.join(' '),
      autores: nomesAutores.join(' '),
      secao: post.data.secao,
      secaoLabel: getSecaoLabel(post.data.secao),
      publicado_em: post.data.publicado_em.toISOString(),
      capa: post.data.capa?.src ?? null,
      url: `/posts/${post.id}`,
      corpo: stripMarkdown(post.body ?? '').slice(0, 2500),
    };
  });

  return new Response(JSON.stringify(documentos), {
    headers: { 'Content-Type': 'application/json' },
  });
};
