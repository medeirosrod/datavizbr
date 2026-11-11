// Luz Coada: as quatro formas das seções (DESIGN.md, "The Four Shapes").
// Todas desenhadas sobre o mesmo módulo de 80 px e devolvidas com coordenadas
// absolutas, para que um degradê em userSpaceOnUse atravesse a parede inteira.

export type Secao = 'bastidores' | 'panorama' | 'praticas' | 'ensaios';

export const SECOES: Secao[] = ['bastidores', 'panorama', 'praticas', 'ensaios'];

/** Caminho SVG da forma da seção, num módulo de 80 px com origem em (x, y). */
export function formaD(secao: Secao, x = 0, y = 0): string {
  const X = (v: number) => +(x + v).toFixed(2);
  const Y = (v: number) => +(y + v).toFixed(2);
  switch (secao) {
    case 'bastidores': // pétala: quatro lentes que se encontram no centro
      return [
        `M${X(40)} ${Y(40)}A24 24 0 0 1 ${X(16)} ${Y(16)}A24 24 0 0 1 ${X(40)} ${Y(40)}Z`,
        `M${X(40)} ${Y(40)}A24 24 0 0 1 ${X(64)} ${Y(16)}A24 24 0 0 1 ${X(40)} ${Y(40)}Z`,
        `M${X(40)} ${Y(40)}A24 24 0 0 1 ${X(64)} ${Y(64)}A24 24 0 0 1 ${X(40)} ${Y(40)}Z`,
        `M${X(40)} ${Y(40)}A24 24 0 0 1 ${X(16)} ${Y(64)}A24 24 0 0 1 ${X(40)} ${Y(40)}Z`,
      ].join('');
    case 'panorama': // círculo de raio 25
      return `M${X(15)} ${Y(40)}a25 25 0 1 0 50 0a25 25 0 1 0 -50 0Z`;
    case 'praticas': // veneziana: três frestas de 50 x 12
      return [16, 34, 52]
        .map((t) => `M${X(21)} ${Y(t)}h38a6 6 0 0 1 0 12h-38a6 6 0 0 1 0 -12Z`)
        .join('');
    case 'ensaios': // losango com vértices a 27 do centro
      return `M${X(40)} ${Y(13)}L${X(67)} ${Y(40)}L${X(40)} ${Y(67)}L${X(13)} ${Y(40)}Z`;
  }
}

/** Tons dos painéis de azulejo e do selo, por seção (DESIGN.md, "Section Palettes"). */
export const PALETA: Record<Secao, { fundo: string; a: string; b: string; forma: string; texto: string }> = {
  bastidores: { fundo: '#c8651a', a: '#fbe3cc', b: '#f4b07a', forma: '#c8651a', texto: '#9a4a0d' },
  panorama:   { fundo: '#552b7b', a: '#e2d2f3', b: '#b9a3d6', forma: '#552b7b', texto: '#552b7b' },
  praticas:   { fundo: '#f4b07a', a: '#9a4a0d', b: '#c8651a', forma: '#9a4a0d', texto: '#7a3a08' },
  ensaios:    { fundo: '#2a1640', a: '#b9a3d6', b: '#d98aa6', forma: '#2a1640', texto: '#2a1640' },
};

export const NOME_SECAO: Record<Secao, string> = {
  bastidores: 'Bastidores',
  panorama: 'Panorama',
  praticas: 'Práticas',
  ensaios: 'Ensaios',
};

export const DESCRICAO_SECAO: Record<Secao, string> = {
  bastidores: 'Como uma visualização foi feita: processo, decisões e ferramentas, em primeira pessoa.',
  panorama: 'Quem faz, o que está acontecendo e quem ganhou o quê na cena brasileira.',
  praticas: 'Princípios, ferramentas e tutoriais aplicáveis, de acessibilidade a software.',
  ensaios: 'O papel da dataviz, ética, futuro e posicionamento no campo.',
};
