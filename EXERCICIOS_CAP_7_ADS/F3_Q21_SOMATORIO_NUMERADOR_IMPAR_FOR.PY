def main ():
    num = 1
    den= 1
    so = 0
    cont = 1
    
    for cont in range(1,51,1):
        
        so += num  / den
        num += 2
        den  += 1
        

    print(f'o valor de S é: {so}')

main()