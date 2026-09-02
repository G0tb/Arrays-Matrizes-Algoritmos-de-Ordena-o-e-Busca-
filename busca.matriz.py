def busca_sequencial_matriz(matriz, valor_procurado):
    """
    Procura 'valor_procurado' em 'matriz' percorrendo linha por linha.

    Retorna: (encontrado, linha, coluna, comparacoes)
    """
    comparacoes = 0
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0

    for i in range(linhas):
        for j in range(colunas):
            comparacoes += 1
            if matriz[i][j] == valor_procurado:
                return True, i, j, comparacoes

    return False, None, None, comparacoes


if __name__ == "__main__":
    exemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    encontrado, linha, coluna, comp = busca_sequencial_matriz(exemplo, 8)
    print(f"Matriz: {exemplo}")
    print(f"Encontrado: {encontrado} | Linha: {linha} | Coluna: {coluna} | Comparações: {comp}")