def main():

    letra = str(input('digite a letra: '))

    vogal_consoante(letra)

def vogal_consoante(letra):

    if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or  letra == 'I' or  letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U':
        print('a letra digitada é uma vogal')
    
    else:
        print('a letra digitada é uma consoante')

main()