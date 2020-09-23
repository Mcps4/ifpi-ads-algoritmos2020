def main():
    num = int(input('Digite quantos numeros você quer digitar: '))
    numeros = [-1] * num
    numeros = lista(num,numeros)

    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('Antes\n')
    print(f'são exatamente: {impar_par(numeros)[0]} numeros pares')
    print(f'são exatamente: {impar_par(numeros)[1]} numeros impares')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(f'são exatamente: {positivo_negativo(numeros)[0]} numeros positivos')
    print(f'são exatamente: {positivo_negativo(numeros)[1]} numeros negativos')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    numeros =  multiplicacao_divisao(num, numeros)
    print('Depois\n')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(f'são exatamente: {impar_par(numeros)[0]} numeros pares')
    print(f'são exatamente: {impar_par(numeros)[1]} numeros impares')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(f'são exatamente: {positivo_negativo(numeros)[0]} numeros positivos')
    print(f'são exatamente: {positivo_negativo(numeros)[1]} numeros negativos')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(f'A media dos numeros é: {media(num,numeros)}')


def lista(num,vet):
    for i in range(num):
        vet[i] = int(input(f'Digite o {i+1}º numero: '))

    return vet

def impar_par(vet):
    par = 0 
    impar = 0
    for i in range(len(vet)):
        if vet[i] % 2 == 0:
            par += 1

        else:
            impar += 1
    impar_e_par = [0] * 2
    impar_e_par[0] = par
    impar_e_par[1] = impar
    return impar_e_par

def positivo_negativo(vet):
    positivo = 0
    negativo = 0
    for i in range(len(vet)):
        if vet[i] >= 0:
            positivo += 1

        else:
            negativo += 1

    positivo_e_negativo = [0] * 2
    positivo_e_negativo[0] = positivo
    positivo_e_negativo[1] = negativo
    return positivo_e_negativo


def multiplicacao_divisao(num, vet):
    for i in range(len(vet)):
        if vet[i] >= 0:
            vet[i] = vet[i] * 2

        else:
            vet[i] = vet[i] / 2

    return vet
            
def media(num, vet):
    soma = 0
    for i in range(num):
        soma += vet[i]

    media = soma / num
    return media 


main()