def main():

    produto_1 = float(input('Digite o preço primeiro produto:'))
    produto_2 = float(input('Digite o preço segundo produto:'))
    produto_3 = float(input('Digite o preço terceiro produto:'))

    precos(produto_1, produto_2, produto_3)
    
def precos(produto_1, produto_2, produto_3):

    if produto_1 < produto_2 and produto_2 < produto_3:
        print('Compre o primeiro produto')

    if produto_2 < produto_1 and produto_1 < produto_3:
        print('Compre o segundo produto')

    if produto_3 < produto_2 and produto_2 < produto_1:
        print('Compre o terceiro produto')

    if produto_1 < produto_3 and produto_3 < produto_2:
        print('Compre o primeiro produto')

    if produto_2 < produto_3 and produto_3 < produto_1:
        print('Compre o segundo produto')

    if produto_3 < produto_1 and produto_1 < produto_2:
        print('Compre o terceiro produto')

    if produto_1 < produto_2 and produto_2 < produto_3:
        print('Compre o primeiro produto')

main()