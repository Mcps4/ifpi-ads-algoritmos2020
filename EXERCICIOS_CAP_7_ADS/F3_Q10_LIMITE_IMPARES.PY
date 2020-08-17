def main():
    n = int(input('digite um numero: '))
    inicio = int(input('Limite inferior: '))
    fim = int(input('Limite superior: '))

    atual = inicio

    while atual <= fim:
        if atual % 2 != 0:
            print(f'>>> {atual}')

        atual = atual + 1

main()