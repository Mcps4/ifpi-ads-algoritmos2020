def main():

    lado_1 = int(input('digite o primeiro lado: '))
    lado_2 = int(input('digite o segundo lado: '))
    lado_3 = int(input('digite o terceiro lado: '))

    verific_triangulo(lado_1, lado_2, lado_3)

def verific_triangulo(lado_1, lado_2, lado_3):
    if lado_1 + lado_2 <= lado_3 or lado_2 + lado_3 <= lado_1 or lado_1 + lado_3 <= lado_2:
        print('nao é um triangulo')

    else:
        if lado_1 == lado_2 == lado_3:
            print('triangulo equilatero')

        elif lado_1 == lado_2 and lado_2 != lado_3 or lado_2 == lado_3 and lado_2 != lado_1:
            print('triangulo isosceles')

        else:
            print('triangulo escaleno')

main()
