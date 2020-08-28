def main():
    n = int(input('digite um numero: '))
    inicio = int(input('Limite inferior: '))
    fim = int(input('Limite superior: '))

    atual = n 

    for atual in range(n,fim + 1,1):
        if atual % n == 0:
            print(f'>>> {atual}')

        


main()