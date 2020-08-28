def main():
    n = int(input('digite a quantidade de numeros: '))
    cont = 1
    sm = 0

    for cont in range (1,n + 1,1):
        num = int(input('digite o numero: '))

        sm = sm + num
        m = sm / n

        

    print(f'A Soma é {sm}')
    print(f'A media é {m}')

    
main()