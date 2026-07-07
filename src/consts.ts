// src/consts.ts
// Constantes globais do projeto. Edite aqui, reflete em todo o site.

export const SITE = {
  nome: 'datavizbr',
  tagline: 'Visualização de dados com sotaque brasileiro',
  descricao: 'Bastidores, panorama, práticas e ensaios sobre visualização de dados em português, desde 2017.',
  url: 'https://datavizbr.com.br',
  idioma: 'pt-BR',
  autor_padrao: 'rodrigo-medeiros',
  email_contato: 'contato@datavizbr.com.br',
  newsletter_url: 'https://eixodatavizbr.beehiiv.com',
};

export const REDES = {
  instagram: 'https://instagram.com/datavizbr',
  twitter:   '',   // adiciona quando tiver Bluesky/Twitter
  github:    '',
};

export const NAV_PRINCIPAL = [
  { texto: 'Bastidores', url: '/bastidores' },
  { texto: 'Panorama',   url: '/panorama'   },
  { texto: 'Práticas',   url: '/praticas'   },
  { texto: 'Ensaios',    url: '/ensaios'    },
  { texto: 'Séries',     url: '/series'     },
  { texto: 'Autores',    url: '/autores'    },
  { texto: 'Tags',       url: '/tags'       },
];

export const NAV_RODAPE = [
  { texto: 'Sobre',    url: '/sobre'          },
  { texto: 'Escrever', url: '/sobre/escrever' },
  { texto: 'Contato',  url: '/sobre/contato'  },
  { texto: 'RSS',      url: '/rss.xml'        },
  { texto: 'Arquivo',  url: '/arquivo'        },
];

export const SECOES_LABELS = {
  bastidores: 'Bastidores',
  panorama: 'Panorama',
  praticas: 'Práticas',
  ensaios: 'Ensaios',
} as const;

export const getSecaoLabel = (secao: string): string => {
  return SECOES_LABELS[secao as keyof typeof SECOES_LABELS] || secao.charAt(0).toUpperCase() + secao.slice(1);
};
