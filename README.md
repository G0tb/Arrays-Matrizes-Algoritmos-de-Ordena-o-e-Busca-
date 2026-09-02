# 📊 Analise Estruturas de Dados
**Arrays, Matrizes, Algoritmos de Ordenação e Busca**

---

## 📑 Sumário
1. ★[Parte 1 - Pesquisa: Bubble Sort vs Quick Sort](#parte-1--pesquisa-bubble-sort-e-quick-sort)
2. ★[Parte 2 - Experimento de Ordenação](#parte-2--experimento-de-ordenação)
3. ★[Parte 3 - Investigação de Busca em Matrizes](#parte-3--investigação-de-busca-em-matrizes)
4. ★[Parte 4 - Hands On 1: Investigação do Array](#parte-4--hands-on-1-investigação-do-array)
5. ★[Parte 5 - Hands On 2: Matriz Aplicada - Monitoramento de Sensores](#parte-5--hands-on-2-matriz-aplicada---monitoramento-de-sensores)
6. ★[Parte 6 - Análise e Conclusão](#parte-6--análise-e-conclusão)

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

* **Notebook no Google Colab:** [Acessar Código da Ordenação](https://colab.research.google.com/drive/11hFjAky0FPpjv9XUbXSqZ0aft8B1TGOq?usp=sharing)

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

* **Notebook no Google Colab:** [Acessar Código de Busca](https://colab.research.google.com/drive/1baMaX1rRTWy69n2iQGN2Wds8iDnEyRya?usp=sharing)

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
  <!-- ESPAÇO PARA SUA RESPOSTA -->

* **e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?**  
  <!-- ESPAÇO PARA SUA RESPOSTA -->

---

## ★ PARTE 4 - Hands On 1: Investigação do Array

### Código Desenvolvido
<!-- Cole aqui o código ou o link para src/parte4_temperaturas.py -->

### Análise e Complexidade
* **Operações de percurso:** <!-- Inserir quantidade de percursos/passos -->
* **Complexidade do algoritmo:** <!-- Inserir complexidade e justificativa -->

---

## ★ PARTE 5 - Hands On 2: Matriz Aplicada - Monitoramento de Sensores

### Código Desenvolvido
<!-- Cole aqui o código ou o link para src/parte5_sensores.py -->

### Respostas Conceituais
* **Por que são necessários loops aninhados?**  
  <!-- ESPAÇO PARA SUA RESPOSTA -->

* **Qual o papel dos índices `[i][j]`?**  
  <!-- ESPAÇO PARA SUA RESPOSTA -->

* **Quantas posições da matriz são percorridas?**  
  <!-- ESPAÇO PARA SUA RESPOSTA -->

* **Qual a relação entre o número de linhas, colunas e quantidade de operações?**  
  <!-- ESPAÇO PARA SUA RESPOSTA -->

---

## ★ PARTE 6 - Análise e Conclusão

* **1. O aumento do tamanho da estrutura de dados influencia a quantidade de operações?**  
  <!-- ESPAÇO PARA SUA RESPOSTA -->

* **2. Bubble Sort e Quick Sort crescem da mesma maneira quando o número de elementos aumenta?**  
  <!-- ESPAÇO PARA SUA RESPOSTA -->

* **3. Por que analisar somente o resultado final da ordenação não é suficiente para comparar algoritmos?**  
  <!-- ESPAÇO PARA SUA RESPOSTA -->
