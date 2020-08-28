def main():
    a0 = int(input('digite o valor de inicio da PA: '))
    l = int(input('digite o valor limite da PA: '))
    r = int(input('digite o valor da razão da PA: '))
    cont = 1
    alvo  = 0
    
    
    for cont in range(alvo + 1, l, 1):
        alvo = a0 + (cont - 1) * r
        if l > alvo:
            print(f'>>> {alvo}')
            

main()