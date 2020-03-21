def main():

    num_1 = int(input('digite o primeiro numero: '))
    num_2 = int(input('digite  o segundo numero: '))
    
    verific_maior_menor(num_1, num_2)

def verific_maior_menor(num_1, num_2):
    if num_1 > num_2:
        print(f'o numero {num_1} é maior que o numero {num_2}')
    
    else:
        print(f'o numero {num_1} é menor que o numero {num_2}')

main()

