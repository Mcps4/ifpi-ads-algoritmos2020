def main():
    n = int(input('digite a quantidade de numeros: '))
    antes = 0
    atual = 1
    cont = 1

    while n >= cont:
        print(atual, end =" ")
        seguinte = atual 
        atual = atual + antes
        antes = seguinte

        cont = cont + 1

main()