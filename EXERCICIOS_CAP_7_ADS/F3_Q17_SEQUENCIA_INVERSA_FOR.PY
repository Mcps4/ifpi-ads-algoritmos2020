def main ():
    n = int(input('digite o valor de n: '))
    cont = 1
    so = 0

    for cont in range(1,n + 1,1):
        so = so + 1 / cont
        

    print(f'o valor de S é: {so}')

main()