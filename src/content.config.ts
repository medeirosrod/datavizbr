// src/content.config.ts
import { defineCollection, reference } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// ---------- AUTORES ----------
const autores = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/autores' }),
  schema: ({ image }) =>
    z.object({
      nome: z.string(),
      foto: image().optional(),
      quem_e: z.string().max(280),
      trabalhando_em: z.string().max(200).optional(),
      trabalho_favorito: z.object({
        titulo: z.string(),
        url: z.string().url(),
      }).optional(),
      por_que_escreveu: z.string().max(400).optional(),
      site: z.string().url().optional(),
      twitter: z.string().optional(),
      instagram: z.string().optional(),
      linkedin: z.string().url().optional(),
      email: z.string().email().optional(),
      papel: z.enum(['curadoria', 'recorrente', 'convidado']).default('convidado'),
      ativo: z.boolean().default(true),
      desde: z.date().optional(),
    }),
});

// ---------- SÉRIES ----------
const series = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/series' }),
  schema: ({ image }) =>
    z.object({
      titulo: z.string(),
      descricao: z.string().max(500),
      capa: image().optional(),
      status: z.enum(['em_andamento', 'encerrada']).default('em_andamento'),
      iniciada_em: z.date(),
      encerrada_em: z.date().optional(),
      cor: z.string().optional(),
    }),
});

// ---------- POSTS ----------
const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: ({ image }) =>
    z.object({
      titulo: z.string(),
      subtitulo: z.string().optional(),
      autores: z.array(reference('autores')).min(1),
      publicado_em: z.date(),
      atualizado_em: z.date().optional(),
      secao: z.enum(['bastidores', 'panorama', 'praticas', 'ensaios']),
      serie: reference('series').optional(),
      ordem_na_serie: z.number().optional(),
      tags: z.array(z.string()).default([]),
      destaque: z.boolean().default(false),
      destaque_na_secao: z.boolean().default(false),
      capa: image().optional(),
      capa_alt: z.string().optional(),
      arquivo: z.boolean().default(false),
      medium_url_original: z.string().url().optional(),
      publicado_originalmente_em: z.date().optional(),
      rascunho: z.boolean().default(false),
      descricao: z.string().max(160).optional(),
    }),
});

// ---------- LIVROS ----------
const livros = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/livros' }),
  schema: ({ image }) =>
    z.object({
      titulo: z.string(),
      subtitulo: z.string().optional(),
      organizadores: z.array(reference('autores')).min(1),
      autores_capitulos: z.array(reference('autores')).optional(),
      ano: z.number(),
      editora: z.string().optional(),
      isbn: z.string().optional(),
      paginas: z.number().optional(),
      idioma: z.enum(['pt-BR', 'en', 'es']).default('pt-BR'),
      sinopse: z.string().max(500),
      capa: image(),
      capa_alt: z.string(),
      tipo_acesso: z.enum(['gratuito', 'pago']),
      formato: z.array(z.enum(['pdf', 'epub', 'impresso', 'web'])),
      links: z.array(z.object({
        tipo: z.enum(['download_pdf', 'download_epub', 'compra', 'leitura_online', 'site_oficial']),
        label: z.string(),
        url: z.string().url(),
      })).default([]),
      sumario: z.array(z.object({
        titulo: z.string(),
        autor: reference('autores').optional(),
        paginas: z.string().optional(),
      })).optional(),
      posts_relacionados: z.array(reference('posts')).optional(),
      publicado_em: z.date(),
    }),
});

export const collections = { autores, series, posts, livros };
