def main():
    n = int(input('digite quantos são os numeros: '))
    cont = 1
    maior = 0 
    atual = 0
    antes = 0

    while cont <= n:
        atual = int(input('digite o numero: '))
        if atual > antes:
            maior  = atual
            antes =  atual
        cont =  cont + 1

    print(f'o maior número é {maior}')


main()