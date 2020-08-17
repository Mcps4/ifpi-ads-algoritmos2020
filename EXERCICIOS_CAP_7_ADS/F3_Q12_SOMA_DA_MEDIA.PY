def main():
    n = int(input('digite a quantidade de numeros: '))
    cont = 1
    sm = 0

    while cont <= n:
        num = int(input('digite o numero: '))

        sm = sm + num
        m = sm / n

        cont = cont + 1

    print(f'A Soma é {sm}')
    print(f'A media é {m}')

    
main()
