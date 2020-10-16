def main():
    n = int(input('Digite quantos elementos você quer na lista: '))
    lista = []
    maior = [0,0]
    menor = [100000000000000,0]
    for i in range(n):
        lista.append(int(input('Digite o elemento da lista: ')))
        if lista[i] > lista[i - 1]:
            maior[0] = lista[i]
            maior[1] = i
        if lista[i] < menor[0]:
            menor[0] = lista[i]
            menor[1] = i

    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(f' o maior numero é {maior[0]} na posicao {maior[1]}')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(f' o menor numero é {menor[0]} na posicao {menor[1]}')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
main()