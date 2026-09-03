# 📊 Analise Estruturas de Dados
**Arrays, Matrizes, Algoritmos de Ordenação e Busca**

---

![Python](https://img.shields.io/badge/Python-3.x-white)
![Status](https://img.shields.io/badge/status-concluído-white )
![Faculdade](https://img.shields.io/badge/disciplina-Estruturas%20de%20Dados-white )
---
## ★ PARTE 1 - Pesquisa: Bubble Sort e Quick Sort

### Bubble Sort
O Bubble Sort é um algoritmo de ordenação que organiza uma lista comparando os elementos que estão lado a lado. Quando estão na ordem errada, eles trocam de posição. Essas comparações são feitas várias vezes, até que todos os elementos estejam em suas posições corretas. No processo, os maiores valores vão sendo levados para o final da lista.

### Quick Sort
O Quick Sort é um algoritmo de ordenação mais eficiente. Ele escolhe um elemento da lista como pivô e divide os outros elementos em dois grupos: os menores e os maiores que o pivô. Depois, o mesmo processo é realizado novamente em cada grupo, até que toda a lista esteja organizada.

### Tabela Comparativa

| Característica | Bubble Sort | Quick Sort |
| :--- | :--- | :--- |
| **Princípio de funcionamento** | Compara da esquerda para a direita, comparando os elementos, fazendo a troca de posições até ordenar | Escolhe um pivô e rearranja em duas metades, de forma que uma parte com os menores valores fique à esquerda e os maiores à direita |
| **Melhor caso** | $\Theta(n)$ | $\Theta(n \log n)$ |
| **Caso médio** | $\Theta(n^2)$ | $\Theta(n \log n)$ |
| **Pior caso** | $\Theta(n^2)$ | $\Theta(n^2)$ |
| **Vantagem principal** | Simples de entender e implementar, consome pouca memória adicional | Super rápido, opera in-place com baixo consumo de memória extra |
| **Limitação principal** | Pouco eficiente para muito volume de dados, consome muito tempo | Não é estável, podendo alterar a ordem original de elementos de valor igual, e é imprevisível no pior caso |
| **Aplicação recomendada** | Vetores menores, ou que já estejam quase ordenados | Grandes volumes de dados onde a velocidade média é prioritária e estabilidade padrão |
| **Aplicação não recomendada** | Ordenações médias a grandes | Listas encadeadas, ou quando é preciso garantia de pior caso, já que pode vir a demorar mais |

---

## ★ PARTE 2 – Experimento de Ordenação

### Tabela de Operações

| Tamanho do Array | Bubble Sort - Comparações | Bubble Sort - Trocas | Quick Sort - Comparações | Quick Sort - Movimentações |
| :---: | :---: | :---: | :---: | :---: |
| **10** | 45 | 20 | 22 | 15 |
| **20** | 190 | 90 | 65 | 45 |
| **1.000** | 499.500 | 250.000 | 10.000 | 6.500 |

### Respostas

* **a) Qual algoritmo realizou menos operações para 10 elementos?**  
  O Quick Sort realizou menos operações que o Bubble Sort.

* **b) O comportamento permaneceu igual para 20 elementos?**  
  Sim. O Quick Sort continuou realizando menos operações que o Bubble Sort.

* **c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?**  
  A diferença ficou muito maior. O Bubble Sort aumentou bastante a quantidade de comparações e trocas, enquanto o Quick Sort cresceu bem menos.

* **d) Qual algoritmo apresentou maior crescimento da quantidade de operações?**  
  O Bubble Sort, pois seu número de operações cresce de forma quadrática, aproximadamente $O(n^2)$.

* **e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?**  
  Sim. Os resultados confirmam a teoria: o Bubble Sort é $O(n^2)$, enquanto o Quick Sort tem complexidade média $O(n \log n)$. Por isso, o Quick Sort tende a ser muito mais eficiente para listas grandes.

* **f) Em qual situação você escolheria Bubble Sort?**  
  Eu escolheria o Bubble Sort para listas pequenas ou quando o objetivo é aprender e entender de forma simples como funciona um algoritmo de ordenação.

* **g) Em qual situação você escolheria Quick Sort?**  
  Eu escolheria o Quick Sort para listas grandes, pois ele geralmente realiza muito menos operações e é mais rápido que o Bubble Sort.

---

## ★ PARTE 3 - Investigação de Busca em Matrizes

### Quantidade de Comparações Realizadas

| Matriz | Nº de elementos | Busca no início | Busca no final | Valor inexistente |
| :---: | :---: | :---: | :---: | :---: |
| **2 × 2** | 4 | 1 | 4 | 4 |
| **10 × 10** | 100 | 1 | 100 | 100 |
| **100 × 100** | 10.000 | 1 | 10.000 | 10.000 |

### Respostas

* **a) Por que encontrar um elemento no início exige menos operações?**  
  Porque a busca sequencial realiza parada imediata no primeiro elemento correspondente.

* **b) O que acontece quando o elemento procurado não existe?**  
  O algoritmo é obrigado a percorrer todas as linhas e colunas para confirmar que não existe na lista, assim fazendo o máximo possível de comparações.

* **c) Qual é o pior caso da busca sequencial?**  
  Ocorre quando o elemento procurado está na última posição ou não existe na matriz.

* **d) Como o aumento das dimensões da matriz influencia a quantidade de operações?**  
  Conforme o tamanho da matriz aumenta, a quantidade de comparações necessárias no pior caso cresce proporcionalmente ao número total de elementos

* **e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?**  
  O(m×n)

---

## ★ PARTE 4 - Hands On 1: Investigação do Array


### Análise e Complexidade
* **Operações de percurso:** O código percorre o array 4 vezes:
*  1 - a entrada de dados 2- na exibição dos valores 3- na busca do maior/menor, 4- na contagem de valores acima da média, então, 4 percursos × 10 elementos, Isso dá  40 operações no total
* **Complexidade do algoritmo:** O(n), pois o número de operações cresce de forma linear com o tamanho do array

---

## ★ PARTE 5 - Hands On 2: Matriz Aplicada - Monitoramento de Sensores

### Código Desenvolvido
<!-- Cole aqui o código ou o link para src/parte5_sensores.py -->

### Respostas Conceituais
* **Por que são necessários loops aninhados?**  
  Porque a matriz tem duas dimensões: é preciso percorrer cada sensor (linha) e, dentro de cada sensor, cada horário (coluna)

* **Qual o papel dos índices `[i][j]`?**  
  O índice i representa o sensor (linha) e o índice j representa o horário (coluna)

* **Quantas posições da matriz são percorridas?**  
  5 × 24 = 120 posições

* **Qual a relação entre o número de linhas, colunas e quantidade de operações?**  
  Quanto mais sensores ou mais horários existirem, mais operações serão necessárias

---

## ★ PARTE 6 - Análise e Conclusão

* **1. O aumento do tamanho da estrutura de dados influencia a quantidade de operações?**  
  Sim. Quanto maior a quantidade de elementos, maior será o número de operações necessárias para realizar a busca ou a ordenação.

* **2. Bubble Sort e Quick Sort crescem da mesma maneira quando o número de elementos aumenta?**  
  Não. O Bubble Sort aumenta as operações mais rapidamente, enquanto o Quick Sort apresenta um crescimento menor e costuma ser mais eficiente quando a quantidade de elementos aumenta.
* **3. Por que analisar somente o resultado final da ordenação não é suficiente para comparar algoritmos?**  
  Porque dois algoritmos podem chegar ao mesmo resultado final, mas realizando quantidades muito diferentes de comparações e trocas, só da pra avaliar a real eficiência de cada um observando o número de operações realizadas durante o processo, não apenas o resultado

  ---
📘 Trabalho desenvolvido para a disciplina de Estruturas de Dados, prof. Karla Sartin — 2026
