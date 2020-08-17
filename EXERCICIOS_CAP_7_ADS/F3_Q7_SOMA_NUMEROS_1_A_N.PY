def main():
    n = int(input('digite um numero: '))
    i = 1
    ac = n

    while i != n:

        ac = ac + (n - 1)
        i = i + 1

    print(f'>>> {ac}')


main()