def main():
    n = int(input('digite um numero: '))
    contador = 0
    alvo = n

    while contador <= alvo:
        if contador % 2 == 0:
            
            print(f'>>> {contador}')
        contador = contador + 1   
main()