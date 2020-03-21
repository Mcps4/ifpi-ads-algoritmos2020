def main():

    dia_1 = int(input('Digite um dia:'))
    mes_1 = int(input('Digite um mes:'))
    ano_1 = int(input('Digite um ano:'))

    dia_2 = int(input('Digite outro dia:'))
    mes_2 = int(input('Digite outro mes:'))
    ano_2 = int(input('Digite outro ano:'))

    data_recente(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2)

def data_recente(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2):

    if ano_1 > ano_2:
        print('A primeira data que você escreveu é a mais recente')

    if ano_2 > ano_1:
        print('A segunda data que você escreveu é a mais recente')

    if ano_1 == ano_2 and mes_1 > mes_2:
        print('A primeira data que você escreveu é a mais recente')

    if ano_1 == ano_2 and mes_2 > mes_1:
        print('A segunda data que você escreveu é a mais recente')

    if ano_1 == ano_2 and mes_1 == mes_2 and dia_1 > dia_2:
     print('A primeira data que você escreveu é a mais recente')

    if ano_1 == ano_2 and mes_1 == mes_2 and dia_2 > dia_1:
        print('A segunda data que você escreveu é a mais recente')

main()