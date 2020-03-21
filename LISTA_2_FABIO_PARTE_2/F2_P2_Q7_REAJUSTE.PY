def main():
    salario = float(input('digite o seu salário: '))

    reajuste(salario)

def reajuste(salario):
    dinheiro_1 = salario + (20 / 100) * salario
    indice_aumento = (20 / 100) * salario

    dinheiro_2 = salario + (15 / 100) * salario
    indice_aumento_2 = (15 / 100) * salario

    dinheiro_3 = salario + (10 / 100) * salario
    indice_aumento_3 = (10 / 100) * salario

    dinheiro_4 = salario + (5 / 100) * salario
    indice_aumento_4 = (5 / 100) * salario
    
    if salario <= 280:

        print(f'o seu salário antes do reajuste é de {salario} reais')
        print('o seu salário teve um aumento percentual de 20 %')
        print(f'o seu salario teve um aumento de {indice_aumento} reais')
        print(f'Seu salário apos o reajuste é de {dinheiro_1} reais')
          
    elif 280 < salario <= 700:
        print(f'o seu salário antes do reajuste é de {salario} reais')
        print('o seu salário teve um aumento percentual de 15 %')
        print(f'o seu salario teve um aumento de {indice_aumento_2} reais')
        print(f'Seu salário após o reajuste é de {dinheiro_2} reais')
          
    elif 700 < salario <= 1500:
        print(f'o seu salário antes do reajuste é de {salario} reais')
        print('o seu salário teve um aumento percentual de 10 %')
        print(f'o seu salario teve um aumento de {indice_aumento_3} reais')
        print(f'Seu salário após o reajuste é de {dinheiro_3} reais')
          
    else:
        print(f'o seu salário antes do reajuste é de {salario} reais')
        print('o seu salário teve um aumento percentual de 5 %')
        print(f'o seu salario teve um aumento de {indice_aumento_4} reais')
        print(f'Seu salário apos o reajuste é de {dinheiro_4} reais')

main()