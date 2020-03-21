def main():
    
    nota_1 = float(input('digite a primeira nota: '))
    nota_2 = float(input('digite a segunda nota: '))
     
    aprovado(nota_1, nota_2)

def aprovado(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2
    
    if media >= 7:
        print('o aluno foi Aprovado')

    else:
        nota_rec = float(input('digite a nota de recuperação: '))
        media_final = (nota_rec + media) / 2
        
        if media_final >= 5:
            print('o aluno foi Aprovado')
    
        else:
            print('o aluno foi reprovado')

main()
        