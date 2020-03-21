def main():

    num_1 = int(input('Informe um numero:'))
    num_2 = int(input('Informe outro numero:'))
    num_3 = int(input('Informe outro numero:'))
    num_4 = int(input('Informe outro numero:'))
    num_5 = int(input('Informe outro numero:'))

    maior_menor(num_1, num_2, num_3, num_4, num_5)

def maior_menor(num_1, num_2, num_3, num_4, num_5):

    if num_1 < num_2 and num_3 and num_4 and num_5:
        print(f'menor Numero é {num_1}')

    elif num_2 < num_1 and num_3 and num_4 and num_5:
        print(f'menor Numero é {num_2}')

    elif num_3 < num_2 and num_1 and num_4 and num_5:
        print(f'menor Numero é {num_3}')

    elif num_4 < num_2 and num_3 and num_1 and num_5:
        print(f'menor Numero é {num_4}')

    elif num_5 < num_2 and num_3 and num_4 and num_1:
        print(f'menor Numero é {num_5}')

    if num_1 > num_2 and num_3 and num_4 and num_5:
        print(f'maior Numero é {num_1}')

    elif num_2 > num_1 and num_3 and num_4 and num_5:
        print(f'maior Numero é {num_2}')

    elif num_3 > num_2 and num_1 and num_4 and num_5:
        print(f'maior Numero é {num_3}')

    elif num_4 > num_2 and num_3 and num_1 and num_5:
        print(f'maior Numero é {num_4}')

    elif num_5 > num_2 and num_3 and num_4 and num_1:
        print(f'maior Numero é {num_5}')

main()