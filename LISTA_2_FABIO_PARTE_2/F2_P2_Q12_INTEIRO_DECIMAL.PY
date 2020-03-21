def main():
    num = float(input('digite o numero: '))

    decimal_inteiro(num)

def decimal_inteiro(num):

    num_2 = num * 10
    unidade = (num_2 // 1) % 10

    if unidade == 0:
        print('o numero é inteiro')
    
    else:
        print('o numero é decimal')

main()