// Registro dos gráficos disponíveis para <Passo grafico="...">.
// Uma série nova adiciona suas entradas aqui.
import VentoPorMes from './VentoPorMes.astro';
import Calendario83Dias from './Calendario83Dias.astro';
import GeraXConsome from './GeraXConsome.astro';
import EolicaPorEstado from './EolicaPorEstado.astro';
import PotenciaAcumulada from './PotenciaAcumulada.astro';

export const graficos = {
  'vento-por-mes': VentoPorMes,
  'calendario-83-dias': Calendario83Dias,
  'gera-x-consome': GeraXConsome,
  'eolica-por-estado': EolicaPorEstado,
  'potencia-acumulada': PotenciaAcumulada,
} as const;

export type IdGrafico = keyof typeof graficos;
