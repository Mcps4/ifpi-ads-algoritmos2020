def main():
    n = int(input('digite um numero: '))
    contador = 0
    alvo = n

    for contador in range(n):
        if contador % 2 == 0:
            
            print(f'>>> {contador}')
           
main()