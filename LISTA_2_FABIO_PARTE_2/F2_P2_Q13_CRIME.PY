def main():

    pgt_1 = str(input('Telefonou para a vítima? '))
    pgt_2 = str(input('Esteve no local do crime? '))
    pgt_3 = str(input('Mora perto da vítima? '))
    pgt_4 = str(input('Devia para a vítima? '))
    pgt_5 = str(input('Já trabalhou com a vítima? '))

    perguntas(pgt_1, pgt_2, pgt_3, pgt_4, pgt_5)
    
def perguntas(pgt_1, pgt_2, pgt_3, pgt_4, pgt_5):

    if pgt_1 and pgt_2 == 'sim' and pgt_1 and pgt_3 != 'sim' and pgt_1 and pgt_4 != 'sim' and pgt_1 and pgt_5 != 'sim':
        print('Suspeita')

    elif pgt_2 and pgt_1 == 'sim' and pgt_2 and pgt_3 != 'sim' and pgt_2 and pgt_4 != 'sim' and pgt_2 and pgt_5 != 'sim':
        print('Suspeita')
    
    elif pgt_3 and pgt_1 == 'sim' and pgt_3 and pgt_2 != 'sim' and pgt_3 and pgt_4 != 'sim' and pgt_3 and pgt_5 != 'sim':
        print('Suspeita')

    elif pgt_4 and pgt_1 == 'sim' and pgt_4 and pgt_2 != 'sim' and pgt_4 and pgt_3 != 'sim' and pgt_4 and pgt_5 != 'sim':
        print('Suspeita')
    
    elif pgt_5 and pgt_1 == 'sim' and pgt_5 and pgt_2 != 'sim' and pgt_5 and pgt_3 != 'sim' and pgt_5 and pgt_4 != 'sim':
        print('Suspeita')
    
    elif pgt_1 == 'sim' and pgt_2 == 'sim' and pgt_3 == 'sim' and pgt_4 == 'sim' and pgt_5 == 'sim':
        print('Assasino')
    
    else:
        print('Cúmplice')


main()