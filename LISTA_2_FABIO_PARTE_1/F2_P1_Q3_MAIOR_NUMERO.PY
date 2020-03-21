def main():

    num_1 = int(input('digite o primeiro numero: '))
    num_2 = int(input('digite  o segundo numero: '))
    num_3 = int(input('digite o terceiro numero: '))

    maior_numero(num_1, num_2, num_3)

def maior_numero(num_1, num_2, num_3):

    if num_1 < num_2 and num_2 < num_3:
        print(f'o maior numero é {num_3}')
    
    elif num_2 < num_1 and num_1 < num_3:
        print(f'o maior numero é {num_3}')

    if num_1 < num_3 and num_3 < num_2:
        print(f'o maior numero é {num_2}')
    
    elif num_3 < num_1 and num_1 < num_2:
        print(f'o maior numero é {num_2}')

    if num_2 < num_3 and num_3 < num_1:
        print(f'o maior numero é {num_1}')
    
    elif num_3 < num_2 and num_2 < num_1:
        print(f'o maior numero é {num_1}')

    else:
        print('dois ou tres numeros são iguais')

main()
