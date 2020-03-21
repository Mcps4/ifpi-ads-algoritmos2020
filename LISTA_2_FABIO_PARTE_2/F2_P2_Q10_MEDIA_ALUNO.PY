def main():
    nota_1 = float(input('digite a sua primeira nota: ')) 
    nota_2 = float(input('digite a sua segunda nota:  '))

    notas(nota_1, nota_2)

def notas(nota_1, nota_2):
    
    media = (nota_1 + nota_2) / 2

    if 9 < media <= 10:
        print('conceito A')
    
    if 7.5 < media <= 9:
        print('conceito B')
    
    if 6 < media <= 7.5:
        print('conceito C')
    
    if 4 < media <= 6:
        print('conceito D')
    
    if 0 < media <= 4:
        print('conceito E')

    if 6 < media <= 10:
        print('Aprovado!')
    
    if media <= 6:
        print('Reprovado!')
    
    print(f'Sua media foi {media}')


main()