def main():

    numero = int(input('Digite um numero de 4 digitos:'))

    quad_perfeito(numero)

def quad_perfeito(numero):
    milhar = numero // 100 
    milhar_2 = milhar * 100
    centena = numero - milhar_2

    if centena + milhar == numero ** 0.5:
        print('É um quadrado perfeito')
    else:
        print('Não é um quadrado perfeito')


main()