def main():
    import math
    n = int(input('digite quantos numeros são: '))
    cont = 1
    atual = 0
    antes = 0

    while cont <= n:
        atual = int(input('digite o numero: '))
        atual = int(math.sqrt(atual))

        if atual > antes:
            maior  = atual
            antes =  atual
            maior = maior ** 2
        cont =  cont + 1

    print(f'o maior quadrado perfeiro menor é {maior}')


main()