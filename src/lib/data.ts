// src/lib/data.ts
import { getCollection, type CollectionEntry } from 'astro:content';

const isProd = import.meta.env.PROD;

// ── POSTS ────────────────────────────────────────────────────────────────────

export async function getPosts() {
  return getCollection('posts', ({ data }) =>
    isProd ? !data.rascunho : true
  );
}

export async function getPostsPorSecao(secao: string) {
  const todos = await getPosts();
  return todos
    .filter((p) => p.data.secao === secao)
    .sort(porData);
}

export async function getPostsPorAutor(idAutor: string) {
  const todos = await getPosts();
  return todos
    .filter((p) => p.data.autores.some((ref) => ref.id === idAutor))
    .sort(porData);
}

export async function getPostsPorSerie(idSerie: string) {
  const todos = await getPosts();
  return todos
    .filter((p) => p.data.serie?.id === idSerie)
    .sort((a, b) => {
      if (a.data.ordem_na_serie && b.data.ordem_na_serie) {
        return a.data.ordem_na_serie - b.data.ordem_na_serie;
      }
      return a.data.publicado_em.valueOf() - b.data.publicado_em.valueOf();
    });
}

export async function getDestaques(limite = 1) {
  const todos = await getPosts();
  return todos
    .filter((p) => p.data.destaque)
    .sort(porData)
    .slice(0, limite);
}

export async function getUltimosPosts(limite = 4) {
  const todos = await getPosts();
  return todos.sort(porData).slice(0, limite);
}

export async function contarPostsPorAutor(): Promise<Map<string, number>> {
  const todos = await getPosts();
  const contagem = new Map<string, number>();
  todos.forEach((post) => {
    post.data.autores.forEach((ref) => {
      contagem.set(ref.id, (contagem.get(ref.id) || 0) + 1);
    });
  });
  return contagem;
}

export async function getAllTags(): Promise<Map<string, number>> {
  const todos = await getPosts();
  const tags = new Map<string, number>();
  todos.forEach((post) => {
    post.data.tags.forEach((tag) => {
      tags.set(tag, (tags.get(tag) || 0) + 1);
    });
  });
  return tags;
}

export async function getPostsPorTag(tag: string) {
  const todos = await getPosts();
  return todos
    .filter((p) => p.data.tags.includes(tag))
    .sort(porData);
}

// ── AUTORES ──────────────────────────────────────────────────────────────────

export async function getAutores() {
  return getCollection('autores', ({ data }) => data.ativo);
}

export async function getAutoresPorPapel() {
  const todos = await getAutores();
  const contagem = await contarPostsPorAutor();

  const curadoria = todos.filter((a) => a.data.papel === 'curadoria');

  const recorrentes = todos
    .filter((a) => a.data.papel !== 'curadoria' && (contagem.get(a.id) || 0) >= 3)
    .sort((a, b) => (contagem.get(b.id) || 0) - (contagem.get(a.id) || 0));

  const convidados = todos
    .filter((a) => a.data.papel !== 'curadoria' && (contagem.get(a.id) || 0) < 3)
    .sort((a, b) => a.data.nome.localeCompare(b.data.nome, 'pt-BR'));

  return { curadoria, recorrentes, convidados };
}

// ── SÉRIES ───────────────────────────────────────────────────────────────────

export async function getSeries() {
  return getCollection('series');
}

export async function getSeriesEmDestaque(limite = 3) {
  const todas = await getSeries();
  return todas.slice(0, limite);
}

// ── LIVROS ───────────────────────────────────────────────────────────────────

export async function getLivros() {
  return getCollection('livros');
}

export async function getLivrosPorAutor(idAutor: string) {
  const livros = await getLivros();
  return livros.filter(
    (l) =>
      l.data.organizadores.some((ref) => ref.id === idAutor) ||
      l.data.autores_capitulos?.some((ref) => ref.id === idAutor)
  );
}

// ── UTILITÁRIOS ──────────────────────────────────────────────────────────────

function porData(
  a: CollectionEntry<'posts'>,
  b: CollectionEntry<'posts'>
) {
  return b.data.publicado_em.valueOf() - a.data.publicado_em.valueOf();
}

export function papelNoLivro(
  livro: CollectionEntry<'livros'>,
  idAutor: string
): 'organizador' | 'autor_capitulo' | null {
  if (livro.data.organizadores.some((r) => r.id === idAutor)) return 'organizador';
  if (livro.data.autores_capitulos?.some((r) => r.id === idAutor)) return 'autor_capitulo';
  return null;
}
