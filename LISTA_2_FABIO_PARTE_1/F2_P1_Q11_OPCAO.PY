def main():

    opcao = float(input('digite a opção: '))
    num_1 = float(input('digite o primeiro número '))
    num_2 = float(input('digite o segundo número: '))
    num_3 = float(input('digite o terceiro número: '))

    opcoes(opcao, num_1, num_2, num_3)

def opcoes(opcao, num_1, num_2, num_3):

    if (opcao == 1 or opcao == 2 or opcao == 3):
        if (opcao == 1):
            print(num_1)

        elif (opcao == 2):
            print(num_2)

        elif (opcao == 3):
            print(num_3)
    else:
        print('opção inválida')
main()