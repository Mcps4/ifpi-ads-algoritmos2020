def main():
    import math

    inicio = int(input('Limite inferior: '))
    fim = int(input('Limite superior: '))

    atual = inicio

    for atual in range (inicio,fim + 1,1):
        if atual == 2:
            print(f'>>> {atual}')

        elif atual % 2 !=  0:

            if atual == 3 or atual == 5 or atual == 7 or atual == 11 or atual == 13 or atual == 17:

                print(f'>>> {atual}')
            
            elif atual % 3 != 0 and atual % 5 != 0 and atual % 7 != 0 and atual % 11 != 0 and atual % 13 != 0 and atual % 17 != 0:

                print(f'>>> {atual}')

        

main()