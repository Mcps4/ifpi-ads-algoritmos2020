def main():
    matriz = def_matriz()
    print_matriz(matriz,'Matriz original:\n')
    s = compor_matriz(matriz)
    valor_maior_soma(s)
    valor_menor_soma(s)

def def_matriz():
    n = int(input('Digite a ordem de sua matriz: '))
    matriz = []
    for i in range(n):
        matriz.append([i] * n)
    return matriz

def compor_matriz(matriz):
    s = [0]* len(matriz)

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input('Digite o valor que você que adicionar a matriz: '))
            s[i] += matriz[i][j]
    print_matriz(matriz,'Matriz preenchida:\n')
    return s

def valor_maior_soma(s):
    maior = s[0]
    valor_maior = 1
    for i in range(1, len(s)):
            if maior < s[i]:
                valor_maior = i + 1
    print(f"O valor maior é: {valor_maior}", )

def valor_menor_soma(s):
    menor = s[0]
    valor_menor = 1
    for i in range(1, len(s)):
            if menor > s[i]:
                valor_menor = i + 1
    print(f"O Valor menor é: {valor_menor}")

def print_matriz(matriz, descrisao):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    for i in range(len(matriz)):
        if i != 0:
            print('',matriz[i])
        else:
            print(descrisao, matriz[i])
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

main()