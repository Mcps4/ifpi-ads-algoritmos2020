def main():
    a0 = int(input('digite o valor de inicio da PG: '))
    l = int(input('digite o valor limite da PG: '))
    r = int(input('digite o valor da razão da PG: '))
    cont = 1
    alvo  = 0
    
    
    for cont in range(alvo + 1,l,1):
        alvo = a0 * r ** (cont - 1)
        if l > alvo:
            print(f'>>> {alvo}')
            

main()