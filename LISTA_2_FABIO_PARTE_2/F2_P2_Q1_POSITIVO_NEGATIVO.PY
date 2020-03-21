def main():

    num = int(input('Digite o numero: '))

    ptv_neg(num)
    
def ptv_neg(num):
    if num > 0:
        print(f'o numero {num} é positivo')

    elif num == 0:
        print('o numero escolhido é zero')
    
    else:
        print(f'o numero {num} é negativo')

main()
        