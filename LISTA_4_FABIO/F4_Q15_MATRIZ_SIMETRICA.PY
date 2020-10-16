def main():
    matriz = def_matriz()
    print_matriz(matriz,'Matriz original:\n')
    matriz = compor_matriz(matriz)
    print_matriz(matriz,'Matriz preenchida:\n')
    print(simetria(matriz))

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

def simetria(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i != j:
                if matriz [i][j] != matriz[j][i]:
                    return 'A matriz digitada não é simetrica'
    return 'A matriz digitada é simetrica'


def print_matriz(matriz, descrisao):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    for i in range(len(matriz)):
        if i != 0:
            print('',matriz[i])
        else:
            print(descrisao, matriz[i])
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')



main()