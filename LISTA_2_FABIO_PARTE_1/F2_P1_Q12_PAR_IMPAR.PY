def main():

    num = int(input('digite o numero: '))

    par_impar(num)

def par_impar(num):
    if num % 2 == 0:
        print(f'o numero {num} é par')
        
    else:
        print(f'o numero {num} é impar')

main()