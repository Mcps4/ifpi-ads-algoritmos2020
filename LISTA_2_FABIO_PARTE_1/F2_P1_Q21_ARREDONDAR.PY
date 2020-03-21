def main():

    num = float(input('digite o  numero: '))

    arredondar(num)

def arredondar(num):
    num_2 = num // 1
    resto = num % num_2
    arre_sup = num_2 + 1

    if resto >= 0.5:
        print(f'{arre_sup}')

    else:
        print(f'{num_2}')

main()
