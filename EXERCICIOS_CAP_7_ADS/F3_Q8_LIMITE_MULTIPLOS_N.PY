def main():
    n = int(input('digite um numero: '))
    inicio = int(input('Limite inferior: '))
    fim = int(input('Limite superior: '))

    atual = n 

    while atual <= fim:
        if atual % n == 0:
            print(f'>>> {atual}')

        atual = atual + 1


main()