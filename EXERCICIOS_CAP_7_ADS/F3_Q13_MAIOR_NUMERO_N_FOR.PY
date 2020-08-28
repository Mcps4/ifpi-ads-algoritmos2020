def main():
    n = int(input('digite quantos são os numeros: '))
    cont = 1
    maior = 0 
    atual = 0
    antes = 0

    for cont in range(1,n + 1,1):
        atual = int(input('digite o numero: '))
        if atual > antes:
            maior  = atual
            antes =  atual
        

    print(f'o maior número é {maior}')


main()