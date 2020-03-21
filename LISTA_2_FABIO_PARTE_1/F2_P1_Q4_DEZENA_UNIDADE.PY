def main():

    numero = int(input('digite o numero: '))

    verific_algarismo(numero)

def verific_algarismo(numero):
    if (numero % 100) // 10 == (numero % 100 ) % 10:
        print(' o algarismo da dezena e da unidade são iguais')
    else:
        print('o algarismo da dezena e da unidade são diferentes')

main()