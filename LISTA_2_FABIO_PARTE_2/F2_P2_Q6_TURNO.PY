def main():
    turno = str(input('digite o turno que você estuda: '))
    horario(turno)
    
def horario(turno):

    if turno == 'matutino':
        print('Bom Dia!')
    
    elif turno == 'vespertino':
        print('Boa Tarde!')
    
    elif turno == 'noturno':
        print('Boa Noite!')
    
    else:
        print('valor inválido')

main()