def main():
    n = int(input('digite o valor de n: '))
    i = n

    while i != 1:

        i = i - 1
        n = n * i

    print(f'>>> {n}' )

main()