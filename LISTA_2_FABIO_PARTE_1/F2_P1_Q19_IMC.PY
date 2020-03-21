def main():

    peso = float(input('digite o seu peso: ')) 
    altura = float(input('digite a sua altura: '))

    imc(peso, altura)

def imc(peso, altura):
    imc = peso / altura ** 2

    if imc < 25:
        print('você está com peso normal')
    
    elif 25 < imc < 30:
        print('você está obeso , procure um médico!')
    
    elif imc > 30:
        prin('você esta com obesidade mórbida, procure um médico com urgência')

main()