def main():
    qtdHoras1 = int(input('Informe a quantidade de horas trabalhadas(prof1):'))
    valorHora1 = float(input('Informe o valor que você recebe por hora trabalhada(prof1):'))
    qtdHoras2 = int(input('Informe a quantidade de horas trabalhadas(prof2):'))
    valorHora2 = float(input('Informe o valor que você recebe por hora trabalhada(prof2):'))

    salario_prof(qtdHoras1, qtdHoras2, valorHora1, valorHora2)

def salario_prof(qtdHoras1, qtdHoras2, valorHora1, valorHora2):

    salario1 = qtdHoras1 * valorHora1
    salario2 = qtdHoras2 * valorHora2

    if salario1 > salario2:
        print('o primeiro professor tem o maior salario')
    if salario2 > salario1:
        print('o segundo professor tem o maior salario')

main()