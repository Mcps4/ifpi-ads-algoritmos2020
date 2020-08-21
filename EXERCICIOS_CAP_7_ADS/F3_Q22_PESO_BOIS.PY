def main():
    n = int(input('digite o numero de gados: '))
    cont = 1
    pe = 0
    nm = 1
    pm = 0
    nme = 1
    pme = 2000

    while cont <= n:
        num = int(input('digite o numero de identificação: '))
        pe = int(input('digite o peso do boi: '))

        if pe > pm:
            nm = num
            pm = pe
            
            
        if pe < pme:
            nme = num
            pme = pe
            

        cont += 1

    print(f'o boi mais pesado tem numero de identificação {nm} e peso {pm} kg')
    print(f'o boi menos pesado tem numero de identificação {nme} e peso {pme} kg')
main()
