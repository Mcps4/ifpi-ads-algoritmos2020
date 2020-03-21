def main():

    dia = int(input('digite o dia: '))
    mes = int(input('digite o mes: '))
    ano = int(input('digite o ano: '))

    data_valida(dia, mes, ano)

def data_valida(dia, mes, ano):
    if  (1 <= dia <= 30) and (1 <= mes <= 12):
        print('a data é valida')

    else:
        print('data é inválida')

main()
    
