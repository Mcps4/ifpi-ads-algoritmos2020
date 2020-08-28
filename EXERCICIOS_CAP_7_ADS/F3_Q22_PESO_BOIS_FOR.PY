def main():
    n = int(input('digite o numero de gados: '))
    cont = 1
    pe = 0
    nm = 1
    pm = 0
    nme = 1
    pme = 2000

    for cont in range(1,n + 1,1):
        num = int(input('digite o numero de identificação: '))
        pe = int(input('digite o peso do boi: '))

        if pe > pm:
            nm = num
            pm = pe
            
            
        if pe < pme:
            nme = num
            pme = pe
            

        

    print(f'o boi mais pesado tem numero de identificação {nm} e peso {pm} kg')
    print(f'o boi menos pesado tem numero de identificação {nme} e peso {pme} kg')
main()
