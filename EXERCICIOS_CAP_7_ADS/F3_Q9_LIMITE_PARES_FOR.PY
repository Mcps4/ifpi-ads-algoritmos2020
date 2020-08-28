def main():
    n = int(input('digite um numero: '))
    inicio = int(input('Limite inferior: '))
    fim = int(input('Limite superior: '))

    atual = inicio

    for atual in range(inicio,fim + 1,1):
        if atual % 2 == 0:
            print(f'>>> {atual}')

        

main()