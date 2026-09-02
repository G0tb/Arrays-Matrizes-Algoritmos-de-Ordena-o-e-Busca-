import random

comp_bubble = 0
trocas_bubble = 0

comp_quick = 0
trocas_quick = 0

# --- ALGORITMO 1: BUBBLE SORT ---
def bubble_sort(lista):
    global comp_bubble, trocas_bubble
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            comp_bubble = comp_bubble + 1
            if lista[j] > lista[j + 1]:

                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                trocas_bubble = trocas_bubble + 1

# --- ALGORITMO 2: QUICK SORT ---
def particionar(lista, inicio, fim):
    global comp_quick, trocas_quick
    pivo = lista[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        comp_quick = comp_quick + 1
        if lista[j] <= pivo:
            i = i + 1

            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            trocas_quick = trocas_quick + 1

    # Coloca o pivô no lugar correto
    aux = lista[i + 1]
    lista[i + 1] = lista[fim]
    lista[fim] = aux
    trocas_quick = trocas_quick + 1

    return i + 1

def quick_sort(lista, inicio, fim):
    if inicio < fim:
        pos_pivo = particio
