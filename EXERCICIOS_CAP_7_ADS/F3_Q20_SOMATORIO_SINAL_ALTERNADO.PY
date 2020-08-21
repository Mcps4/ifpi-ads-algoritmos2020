def main ():
    n = int(input('digite o valor de n: '))
    cont = 1
    so = 0

    while cont <= n:
        if cont % 2 != 0:
            so = so + 1 / cont

        else:
            so  = so - 1 / cont
        cont += 1

    print(f'o valor de S é: {so}')

main()