import math
def main():

    letra_a = int(input('digite o valor de a: '))
    letra_b = int(input('digite o valor de b: '))
    letra_c = int(input('digite o valor de c: '))

    raizes(letra_a, letra_b, letra_c)

def raizes(letra_a, letra_b, letra_c):
    delta = letra_b ** 2 - 4 * letra_a * letra_c
    raiz_1 = (- letra_b + delta ** 0.5) / (2 * letra_a)
    raiz_2 = (- letra_b - delta ** 0.5) / (2 * letra_a)

    if letra_a != 0:
        print(f'a equação tem como raizes os numeros {raiz_1} e {raiz_2}')
    
    else:
        print('a equação nao tem raizes')

main()