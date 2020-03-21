def main():

    valor_hora = float(input('digite o valor cobrado pela hora: '))
    qtd_horas = int(input('digite a quantidade de horas trabalhadas: '))

    impostos(valor_hora, qtd_horas)

def impostos(valor_hora, qtd_horas):

    salario_bruto = valor_hora * qtd_horas
    inss = (10 / 100) * salario_bruto
    fgts = (11 / 100) * salario_bruto
    salario_liquido_1 = salario_bruto - inss

    ir_1 = (5 / 100) * salario_bruto 
    total_descontos_1 = ir_1 + inss
    salario_liquido_2 = salario_bruto - total_descontos_1

    ir_2 = (10 / 100) * salario_bruto
    total_descontos_2 = ir_2 + inss
    salario_liquido_3 = salario_bruto - total_descontos_2

    ir_3 = (20 / 100) * salario_bruto
    total_descontos_3 = ir_3 + inss
    salario_liquido_4 = salario_bruto - total_descontos_3
    
    if salario_bruto <= 900:
        print(f'Salário Bruto      :R$ {salario_bruto}')
        print(f'IR (0 %)           : isento')
        print(f'INSS(10 %)         :R$ {inss}')
        print(f'FGTS(11 %)         :R$ {fgts}')
        print(f'Total de descontos :R$ {inss}')
        print(f'Salário Liquido    :R$ {salario_liquido_1}')
    
    elif 900 < salario_bruto <= 1500:
        print(f'Salário Bruto      :R$ {salario_bruto}')
        print(f'IR (5 %)           :R$ {ir_1}')
        print(f'INSS(10 %)         :R$ {inss}')
        print(f'FGTS(11 %)         :R$ {fgts}')
        print(f'Total de descontos :R$ {total_descontos_1}')
        print(f'Salário Liquido    :R$ {salario_liquido_2}')

    elif 1500 < salario_bruto <= 2500:
        print(f'Salário Bruto      :R$ {salario_bruto}')
        print(f'IR (10 %)          :R$ {ir_2}')
        print(f'INSS(10 %)         :R$ {inss}')
        print(f'FGTS(11 %)         :R$ {fgts}')
        print(f'Total de descontos :R$ {total_descontos_2}')
        print(f'Salário Liquido    :R$ {salario_liquido_3}')
    
    else:
        print(f'Salário Bruto      :R$ {salario_bruto}')
        print(f'IR (20 %)          :R$ {ir_3}')
        print(f'INSS(10 %)         :R$ {inss}')
        print(f'FGTS(11 %)         :R$ {fgts}')
        print(f'Total de descontos :R$ {total_descontos_3}')
        print(f'Salário Liquido    :R$ {salario_liquido_4}')

main()