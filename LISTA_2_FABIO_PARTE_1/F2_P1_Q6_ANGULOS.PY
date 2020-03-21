def main():

    alg_1 = int(input('digite o primeiro angulo: '))
    alg_2 = int(input('digite  o segundo angulo: '))
    alg_3 = int(input('digite o terceiro angulo: '))

    angulos(alg_1, alg_2, alg_3)

def angulos(alg_1, alg_2, alg_3):
    if alg_1 + alg_2 + alg_3 < 180 or alg_1 + alg_2 + alg_3 > 180:
        print('nao é um triangulo')

    else:

        if alg_1 < 90 and alg_2 < 90 and alg_3 < 90:
            print('triangulo acuntangulo')

        elif alg_1 == 90 or alg_2 == 90 or alg_3 == 90:
            print('triangulo retangulo')
        
        elif alg_1 > 90 or alg_2 > 90 or alg_3 > 90:
            print('triangulo obtusangulo')

main()

        

    
    