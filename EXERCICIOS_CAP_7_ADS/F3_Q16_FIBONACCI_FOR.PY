def main():
    n = int(input('digite a quantidade de numeros: '))
    antes = 0
    atual = 1
    cont = 1

    for n in range(cont,n + 1,1):
        print(atual, end =" ")
        seguinte = atual 
        atual = atual + antes
        antes = seguinte

        

main()