def main():
    matriz = def_matriz()
    print_matriz(matriz,'Matriz original:\n')
    matriz = compor_matriz(matriz)
    print_matriz(matriz,'Matriz preenchida:\n')
    dgn_principal = resultado_dgn_principal(matriz)
    dgn_secundaria = resultado_dgn_secundaria(matriz)

def def_matriz():
    n = int(input('Digite a ordem de sua matriz: '))
    matriz = []
    for i in range(n):
        matriz.append([i] * n)
    return matriz

def compor_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input('Digite o valor que você que adicionar a matriz: '))
    return matriz

def resultado_dgn_principal(matriz):
    s = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                s += matriz[i][j]
    return s

def resultado_dgn_secundaria(matriz):
    s = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i + j) == (len(matriz) - 1):
                s += matriz[i][j]
    return s

def print_matriz(matriz, descrisao):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    for i in range(len(matriz)):
        if i != 0:
            print('',matriz[i])
        else:
            print(descrisao, matriz[i])
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')




main()