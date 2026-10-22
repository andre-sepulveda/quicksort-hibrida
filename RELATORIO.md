# Relatório — Quicksort híbrida com insertion sort

## Metodologia

- Tamanho do vetor: **20,000 elementos**.
- Valores gerados aleatoriamente com semente fixa: **20261022**.
- Repetições por configuração: **7**; foi usada a mediana dos tempos.
- Cada execução recebeu uma cópia do mesmo vetor; a cópia e a geração dos dados ficaram fora da medição.
- A quicksort usa pivô aleatório e partição em três grupos: menores, iguais e maiores que o pivô.
- Quando o trecho tem menos de `corte` elementos, é aplicado insertion sort.
- O caso `corte = 1` não aciona insertion sort para trechos de tamanho 1 ou maior e serve como baseline da quicksort pura.

## Resultados

| Corte | Tempo mediano (ms) | Diferença vs. corte 1 |
|---:|---:|---:|
| 1 | 27.668 | +0.00% |
| 5 | 25.588 | -7.52% |
| 10 | 24.679 | -10.81% |
| 16 | 24.180 | -12.61% |
| 20 | 26.100 | -5.67% |
| 32 | 23.803 | -13.97% |
| 50 | 25.240 | -8.78% |
| 100 | 32.043 | +15.81% |
| 200 | 46.913 | +69.55% |

## Análise

- **Melhor corte observado:** `32`, com tempo mediano de **23.803 ms**.
- **Ganho em relação à quicksort pura:** 12.87% (medianas: 46.578 ms contra 40.585 ms).
- **Cortes grandes demais:** o insertion sort tem custo quadrático no tamanho do trecho. Quando o corte fica alto, ele pode ordenar trechos relativamente grandes por inserção, aumentando o trabalho e piorando o tempo. O ponto ideal depende dos dados, da implementação e da máquina.
- **Corte = 1:** comporta-se como a quicksort pura nesta implementação, pois não chama insertion sort para subvetores de tamanho positivo. Diferenças pequenas de tempo podem ocorrer por ruído de medição.
