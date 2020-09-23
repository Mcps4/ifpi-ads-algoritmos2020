def main():
    menu = '##### WordPlay #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Palavras e letras proibidas\n' \
        + '4 - Palavras com letras pré-definidas\n' \
        + '5 - Palavras com letras obrigatórias\n'\
        + '6 - Palavras em ordem alfabética\n' \
        + '0 - Sair\n' \
        + '\nDigite uma opção: '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            palavras_com_mais_de_20_letras()
        elif opcao == 2:
            palavras_sem_letra_e()

        elif opcao == 3:
            letras_palavras_proibidas()

        elif opcao == 4:
            palavra_letra_definida()

        elif opcao == 5:
            palavras_com_letras_obrigatórias()

        elif opcao == 6:
            palavras_ordem_alfabetica()

        else:
            print('Opção Inválida!')

        input('continuar <enter> ...')
        opcao = int(input(menu))

    print('Fim wordplay....')


def palavras_com_mais_de_20_letras():
    print('>> Palavras com + de 20 letras \n')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


def palavras_sem_letra_e():
    print('>> Palavras sem letra "e" \n')
    arquivo = open('words.txt')
    total = 0
    palavras_sem_e = 0

    for linha in arquivo:
        palavra = linha.strip()
        total += 1
        if has_no_e(palavra):
            palavras_sem_e += 1
            print(palavra)

    perc = (palavras_sem_e / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras sem "e": {palavras_sem_e}')
    print(f'Percentual {perc} %')
    arquivo.close()


def has_no_e(palavra):
    for l in palavra:
        if l == 'e':
            return False

    return True

def letras_palavras_proibidas():
    print('>> Palavras e Letras Proibidas \n')
    arquivo = open('words.txt')
    letra = input('Digite as letras proibidas: ')
    palavras = 0
    for linha in arquivo:
        palavra = linha.strip()
        if avoids(palavra, letra):
            palavras += 1
            print(palavra)

    porcentagem = (palavras / 113809.0) * 100
    arquivo.close()
    print (f"A porcentagem é igual a: {porcentagem}")

def avoids(palavra,letra):
    for i in palavra:
        if i in letra:
            return False
    return True

def palavra_letra_definida():
    print('>> Palavras com letras pré-definidas\n')
    arquivo = open('words.txt')
    letras = input('Digite as letras: ')
    for linha in arquivo:
        palavra = linha.strip()
        if uses_only(palavra, letras):
            print(palavra)

def uses_only(palavra, letras):
    for letra in palavra:
        if letra not in letras:
            return False
    return True

def palavras_com_letras_obrigatórias():
    print('>> Palavras com letras obrigatórias\n')
    arquivo = open('words.txt')
    letras = input('Digite as letras: ')
    for linha in arquivo:
        palavra = linha.strip()
        if uses_all(palavra, letras):
            print(palavra)

def uses_all(palavra, letras):
    for letra in letras:
        if letra not in palavra:
            return False
    return True

def palavras_ordem_alfabetica():
    print('>> Palavras em ordem alfabética\n')
    arquivo = open('words.txt')
    for linha in arquivo:
        palavra = linha.strip()
        if is_abecedarian(palavra):
            print(palavra)


def is_abecedarian(palavra):
    for i in range(0,len(palavra)-1):
        if not palavra[i] <= palavra[i+1]:
            return False
    return True
    
main()