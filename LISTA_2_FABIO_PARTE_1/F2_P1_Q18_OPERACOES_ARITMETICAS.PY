def main():

    valor_1 = float(input('digite o primeiro valor: '))
    valor_2 = float(input('digite o segundo valor: '))
    operacao = int(input('digite a operação aritmetica que deseja executar: '))

    operacoes(valor_1, valor_2, operacao)

def operacoes(valor_1, valor_2, operacao):

    opr_1 = valor_1 + valor_2
    opr_2 = valor_1 - valor_2
    opr_3 = valor_1 * valor_2
    opr_4 = valor_1 / valor_2

    if (operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4):

        if (operacao == 1):
            print(opr_1)

        elif (operacao == 2):
            print(opr_2)

        elif (operacao == 3):
            print(opr_3)

        elif (operacao == 4):
            print(opr_4)

    else:
        print('operação inválida!')

            
main()
    