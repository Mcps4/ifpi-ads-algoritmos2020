def main():

    senha = int(input('Digite a senha: '))

    codigo(senha)

def codigo(senha):

    if senha == 1234:
        print('Senha válida')

    else:
        print('Senha inválida')

main()