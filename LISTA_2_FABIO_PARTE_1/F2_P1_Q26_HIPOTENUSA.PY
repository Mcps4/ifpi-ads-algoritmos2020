def main():
    lado_1 = int(input('Digite o primeiro lado do triangulo: '))
    lado_2 = int(input('Digite o segundo lado do triangulo: '))
    lado_3 = int(input('Digite o terceiro lado do triangulo: '))

    hipotenusa(lado_1, lado_2, lado_3)

def hipotenusa(lado_1, lado_2, lado_3):

    if lado_1 > lado_2 and lado_3:
        print(f'{lado_1} é a hipotenusa e {lado_2} e {lado_3} são os catetos')

    if lado_2 > lado_1 and lado_3:
        print(f'{lado_2} é a hipotenusa e {lado_1} e {lado_3} são os catetos')

    if lado_3 > lado_2 and lado_1:
        print(f'{lado_3} é a hipotenusa e {lado_2} e {lado_1} são os catetos')

main()