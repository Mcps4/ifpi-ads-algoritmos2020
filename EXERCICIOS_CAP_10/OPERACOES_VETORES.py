def main():

    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - mostrar todos os valores'
    menu += '\n 4 - Remover final, inicio, posicao especifica'
    menu += '\n 5 - inserir valores em posição especifica'
    menu += '\n 6 - Numero de pares, impares, primos, positivos, nulos'
    menu += '\n 7 - Media dos valores'
    menu += '\n 8 - Quantidade  de ocorrencias do valor'
    menu += '\n 9 - Dobrar os valores'
    menu += '\n 10 -Dobrar valores multiplos de N'
    menu += '\n 11 - Apagar valores'
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:  
        opcao = int(input(menu))

        
        if opcao == 1:
            inserir_valores(lista)
        elif opcao == 2:
            mostra_valor(lista)
        elif opcao == 3:
            mostrar_todos_valores(lista)

        elif opcao == 4:
            remover(lista)

        elif opcao == 5:
            inserir_posicao_especifica(lista)
        
        elif opcao == 6:
            numeros(lista)

        elif opcao == 7:
            media(lista)

        elif opcao == 8:
            qtd_ocorrencia(lista)

        elif opcao == 9:
            dobrar(lista)

        elif opcao == 10:
            multiplos(lista)

        elif opcao == 11:
            delete(lista)

        elif opcao == 0:
            break
        else:
            print('Opção Inválida')


def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir? '))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')
    input('<enter> to continue...')


def mostra_valor(lista):
    posicao = int(input('Qual posição? '))
    print('Valor buscado:')
    print(lista[posicao])

    input('<enter> to continue...')

def mostrar_todos_valores(lista):
    print(lista)

    input('<enter> to continue...')

def remover(lista):
    remover = '>>> Digite o que voce quer remover >>>'
    remover = '\n 0 - Sair'
    remover = '\n 1 - Remover Inicio'
    remover = '\n 2 - Remover Final'
    remover = '\n 3 - Remover Posição especifica'

    remover_lista = int(input(remover))

    if remover_lista == 1:
        lista.pop(0)

    elif remover_lista == 2:
        lista.pop(len(lista) - 1)

    elif remover_lista == 3:
        index = int(input('Digite o index do item da lista que você quer remover: '))
        lista.pop(index)
    elif remover_lista == 0:
        input('<enter> to continue...')
    else:
        print('Opção inválida')

def inserir_posicao_especifica(lista):
    index = int(input('Digite o index que você quer inserir: '))
    lista[index] = int(input(f'Digite o numero que você quer inserir no index {index}: '))

def numeros(lista):
    numero = '>>> Digite o que voce quer remover >>>'
    numero = '\n 0 - Sair'
    numero = '\n 1 - Numeros Pares'
    numero = '\n 2 - Numeros Impares'
    numero = '\n 3 - Numeros Primos'
    numero = '\n 4 - Numeros Positivos'
    numero = '\n 5 - Numeros negativos'
    numero = '\n 6 - Numeros nulos'

    id_numeros = int(input(numero))

    if  id_numeros == 1:
        pares = 0
        for i in range(len(lista)):
            if i % 2 == 0:
                pares += 1
            print(f'quantidade de numeros pares: {pares} ')
            
    elif id_numeros == 2:
        impares = 0
        for i in range(len(lista)):
            if i % 2 != 0:
                impares += 1
            print(f'quantidade de numeros impares: {impares} ')

    elif id_numeros == 3:
        print(f'quantidade de numeros primos: ' , e_primo(lista))

    elif id_numeros == 4:
        positivos = 0
        for i in range(len(lista)):
            if i > 0:
                positivos += 1
            print(f'quantidade de numeros positivos: {positivos} ')

    elif id_numeros == 5: 
        negativos = 0    
        for i in range(len(lista)):
            if i < 0:
                negativos += 1
            print(f'quantidade de numeros negativos: {negativos}')

    elif id_numeros == 6:
        nulos = 0
        for i in range(len(lista)):
            if i == 0:
                nulos += 1
            print(f'quantidade de numeros nulos: {nulos}')

    elif id_numeros == 0:
        input('<enter> to continue...')
    else:
        print('Opção inválida')

def e_primo(lista):
    primos = int(0)
    for i in lista:
        primos += primo(i)
    return primos

def primo(n):
    acum = 0
    for i in range(1, n + 1, 1):
        if n % i == 0:
            acum += 1
        
    if acum == 2:
        return int(1)
    else:
        return int(0)

def media(lista):
    soma = 0
    for i in lista:
        soma += 1
    media = soma / len(lista)

    print(f'A media dos valores da lista é: {media}')

def qtd_ocorrencia(lista):
    ac = 0
    qtd = input('Digite o item que você quer identificar a quantidade de ocorrencias: ')
    for i in lista:
        if i == qtd:
            ac += 1

        print(f'A quantidade de ocorrencias do numero escolhido é: {ac}')

def dobrar(lista):
    c = 0
    dobrado = []
    for i in lista:
        dobrado.append(i * 2)
        c += 1
    print(f'Antes: {lista}')
    print(f'dobrado: {dobrado}')
    input('<enter> to continue...')

def multiplos(lista):
    num = int(input('Digite o valor que você quer identificar se um item da lista é multiplo: '))
    dobrado = []
    for i in lista:
        if i % num == 0:
            dobrado.append(i * 2)

        else:
            dobrado.append(i)
        c += 1

    print(f'Antes: {lista}')
    print(f' O dobro dos Multiplos de: {num} é {dobrado}')
    input('<enter> to continue...')

def delete(lista):
    lista.clear()
    input('<enter> to continue...')


main()