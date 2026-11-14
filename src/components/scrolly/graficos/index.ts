// Registro dos gráficos disponíveis para <Passo grafico="...">.
// Uma série nova adiciona suas entradas aqui.
import VentoPorMes from './VentoPorMes.astro';
import Calendario83Dias from './Calendario83Dias.astro';
import GeraXConsome from './GeraXConsome.astro';
import EolicaPorEstado from './EolicaPorEstado.astro';
import PotenciaAcumulada from './PotenciaAcumulada.astro';
import SedesNordeste from './SedesNordeste.astro';
import ExpansaoBrasil from './ExpansaoBrasil.astro';
import PernambucoCampi from './PernambucoCampi.astro';
import Patentes30 from './Patentes30.astro';
import PatentesEvolucao from './PatentesEvolucao.astro';
import Nota7 from './Nota7.astro';

export const graficos = {
  'vento-por-mes': VentoPorMes,
  'calendario-83-dias': Calendario83Dias,
  'gera-x-consome': GeraXConsome,
  'eolica-por-estado': EolicaPorEstado,
  'potencia-acumulada': PotenciaAcumulada,
  'sedes-nordeste': SedesNordeste,
  'expansao-brasil': ExpansaoBrasil,
  'pernambuco-campi': PernambucoCampi,
  'patentes-30': Patentes30,
  'patentes-evolucao': PatentesEvolucao,
  'nota-7': Nota7,
} as const;

export type IdGrafico = keyof typeof graficos;
