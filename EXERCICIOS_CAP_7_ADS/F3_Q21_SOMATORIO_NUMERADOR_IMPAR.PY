def main ():
    num = 1
    den= 1
    so = 0
    cont = 1
    
    while cont <= 50:
        
        so += num  / den
        num += 2
        den  += 1
        cont += 1

    print(f'o valor de S é: {so}')

main()