def main():

    numero = int(input('Digite um numero de 4 digitos: '))

    dividir_numero(numero)

def dividir_numero(numero):
    milhar = numero // 100 
    milhar_2 = milhar * 100
    centena = numero - milhar_2

    if (centena + milhar) ** 2 == numero:
        print('entao o numero existe')
    
    else:
        print('o numero nao existe')

main()

