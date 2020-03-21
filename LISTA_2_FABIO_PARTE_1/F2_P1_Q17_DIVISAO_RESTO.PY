def main():

    num_1 = int(input('digite um numero:'))
    num_2 = int(input('digite outro numero:'))

    num_3 = num_1 + num_2 + 1
    num_4 = (num_1 + num_2) * num_1
    num_5 = (num_1 + num_2) / 2
    num_6 = num_1 ** 2   
    num_7 = num_2 ** 2

    divisao(num_1,num_2)

def divisao(num_1,num_2):
    if num_1 % num_2 == 1:
        print(f'{num_3}')

    elif num_1 % num_2 == 2 and num_1 % 2 == 0:
        print('Os numeros são pares')

    if num_1 % num_2 == 2 and num_1 % 2 != 0:
        print('Os numeros são impares')

    if num_1 % num_2 == 3:
        print(f'{num_4}')

    if num_1 % num_2 == 4:
        print(f'{num_5}')

    elif num_1 % num_2 == 0 or num_1 % num_2 > 4:
        print(f'{num_6} e {num_7}')

main()
