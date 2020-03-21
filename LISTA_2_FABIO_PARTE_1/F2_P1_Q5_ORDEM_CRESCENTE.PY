def main():
    num_1 = int(input('digite o primeiro numero: '))
    num_2 = int(input('digite  o segundo numero: '))
    num_3 = int(input('digite o terceiro numero: '))

    ordem_crescente(num_1, num_2, num_3)

def ordem_crescente(num_1, num_2, num_3):
    if num_1 < num_2 < num_3:
        print(f'{num_1}, {num_2}, {num_3}')

    if num_1 < num_3 < num_2:
        print(f'{num_1}, {num_3}, {num_2}')

    if num_2 < num_1 < num_3:
        print(f'{num_2}, {num_1}, {num_3}')

    if num_2 < num_3 < num_1:
        print(f'{num_2}, {num_3}, {num_1} ')

    if num_3 < num_2 < num_1:
        print(f'{num_3}, {num_2}, {num_1}')

    if num_3 < num_1 < num_2:
        print(f'{num_3}, {num_1}, {num_2}')

       
main()