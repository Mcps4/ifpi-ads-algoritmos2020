def main():

    angulo = int(input('Digite um ângulo entre 0 e 360:'))

    quadrante(angulo)

def quadrante(angulo):

    if angulo < 90:
        print('Primeiro quadrante')

    elif angulo != 90 and angulo < 180:
        print('Segundo quadrante')

    elif angulo != 180 and angulo < 270:
        print('Terceiro quadrante')

    elif angulo != 270 and angulo < 360:
        print('Quarto quadrante')

    else:
        print('Não pertence a nenhum quadrante')

main()