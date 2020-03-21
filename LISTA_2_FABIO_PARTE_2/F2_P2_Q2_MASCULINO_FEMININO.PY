def main():

    letra = str(input("Fale seu sexo:"))
   
    sexo(letra)

def sexo(letra):
    M = 'masculino'
    F = 'feminino'

    if letra == M:
        print('Seu sexo é masculino')

    elif letra == F:
        print('Seu sexo é feminino')

    else:
        print('sexo inválido')

main()