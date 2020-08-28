def main():
    num_f = int(input('digite quantos funcionarios trabalham na empresa: '))
    

    cont = 1
    for cont in range(1,num_f + 1,1):
        cod = int(input('digite o codigo do funcionario: '))
        num_h = int(input('digite o numero de horas trabalhadas: '))
        num_d = int(input('digite o numero de dependentes: '))

        sa = 12 * num_h + 40 * num_d
        desc_1 = sa * 0.085
        desc_2 = sa * 0.05
        sl = float(sa - desc_1 - desc_2)
        

        print('>>'* 50)
        print(f'descontos: inss = {desc_1}, IR = {desc_2}')
        print(f'O sálario liquido é: {sl}')
        print('>>'* 50)
        
main()