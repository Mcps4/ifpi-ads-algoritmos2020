def main():

    num_1 = int(input('digite o primeiro numero: '))
    num_2 = int(input('digite  o segundo numero: '))
    num_3 = int(input('digite o terceiro numero: '))
    num_4 = int(input('digite o quarto numero: '))
    num_5 = int(input('digite o quinto numero: '))

    maior_media(num_1, num_2, num_3, num_4, num_5)

def maior_media(num_1, num_2, num_3, num_4, num_5):
    media = (num_1 + num_2 + num_3 + num_4 + num_5) / 5

    if num_1 > media:
        print(f'o numero {num_1}')
    
    if num_2 > media:
        print(f'o numero {num_2}')

    if num_3 > media:
        print(f'o numero {num_3}')

    if num_4 > media:
        print(f'o numero {num_4}')

    if num_5 > media:
        print(f'o numero {num_5}')

main()