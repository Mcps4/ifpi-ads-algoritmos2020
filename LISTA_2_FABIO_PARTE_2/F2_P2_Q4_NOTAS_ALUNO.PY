def main():

    nota_1 = float(input('Digite sua primeira nota:'))
    nota_2 = float(input('Digite sua segunda nota:'))

    notas(nota_1, nota_2)

def notas(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2

    if media >= 7 and media != 10:
        print('Aprovado!')

    if media < 7:
        print('Reprovado!')

    if media == 10:
        print('Aprovado com distinção!')

main()