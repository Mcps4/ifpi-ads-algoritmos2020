def main():
    n = int(input('digite o valor de n: '))
    i = n

    for i in range(2, n + 1):

        i = i - 1
        n = n * i

    print(f'>>> {n}' )

main()