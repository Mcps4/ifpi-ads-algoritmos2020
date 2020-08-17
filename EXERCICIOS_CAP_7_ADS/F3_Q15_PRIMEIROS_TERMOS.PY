def main():
    n = int(input('digite a quantidade de numeros: '))
    cont = 1
    r = 1
    
    while n >= r:
        print(f'>>> {cont}')
        r = r + 1
        cont = r + cont
        

        
main()