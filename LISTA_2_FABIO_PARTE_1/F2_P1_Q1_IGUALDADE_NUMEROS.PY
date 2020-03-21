def main():

    num_1 = int(input('digite o primeiro numero: '))
    num_2 = int(input('digite  o segundo numero: '))
    num_3 = int(input('digite o terceiro numero: '))
    verifique_igualdade(num_1, num_2, num_3)

def verifique_igualdade(num_1, num_2, num_3):
    if num_1 == num_2 == num_3:
        print('os tres numeros sao iguais')

    elif (num_1 == num_2 or num_2 == num_3 or num_1 == num_3):
        print('existem dois numeros iguais')

    else:
        print('todos os numeros sao diferentes')

main()