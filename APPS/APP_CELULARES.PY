import os
import json
def main():
    celulares = inicializar('celulares.bd')

    menu = main_screen()
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            print(' Novo celular')
            celular = novo_celular()
            celulares.append(celular)
            print('Celular cadastrado com sucesso!')

        elif opcao == 2:
            mostrar_celulares(celulares)

        elif opcao == 3:
            pesquisar_celular(celulares)

        input('<Enter>')
        opcao = int(input(menu))

    finalizar('celulares.bd', celulares)

def main_screen():
    menu = '>>>>>>>> Opçoes da Lista >>>>>>>>\n'
    menu += '1 - Criar Novo celular\n'
    menu += '2 - Listar celulares cadastrados\n'
    menu += '3 - selecionar celulares cadastrados\n'
    menu += '0 - Sair\n'

    menu += 'opcao >>> '
    return menu

def novo_celular():
            nome = input('nome: ')
            marca = input('Marca: ')
            tela = input('Tela("): ')
            valor = float(input('Valor(R$): '))
            cam_frontal = input('Camera Frontal(sim/não): ')

            celular = {}
            celular['nome'] = nome
            celular['marca'] = marca
            celular['tela'] = tela
            celular['valor'] = valor
            celular['cam_frontal'] = cam_frontal

            
            return celular

def mostrar_celulares(celulares):
    qtd = len(celulares)
    print(f'Listando {qtd} celulares')

    for celular in celulares:
        print('Nome:', celular['nome'])
        print('Marca:', celular['marca'])
        print('Tela:', celular['tela'])
        print('Valor:', celular['valor'])
        print('Cam_frontal:', celular['cam_frontal'])
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def inicializar(nome_arquivo):
    celulares_carregados = []
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        arquivo.close()
        celulares_carregados = json.loads(dados)

    return celulares_carregados

def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close

def pesquisar_celular(celulares):
    pesquisar = input('Digite a marca ou o nome do smartphone: ')
    i = 0
    for celular in celulares:
        if pesquisar in celular['nome']:
            print(30*'>>>')
            print('código: 00 -', i)
            print('Nome:', celular['nome'] )
            print('Marca:', celular['marca'])

        elif pesquisar in celular['marca']:
            print(30*'>>>')
            print('código: 00 -', i)
            print('Nome:', celular['nome'])
            print('Marca:', celular['marca'])
        i += 1
    prosseguir = input('Digite se você deseja selecionar algum celular (Sim/Não): ')
    prosseguir = prosseguir.upper()
    
    if prosseguir == 'SIM':
        selecionado = int(input('Digite o codigo do celular da lista que deseja selecionar: '))
        selecionar_celular(celulares, selecionado)

def selecionar_celular(celulares, selecionado):
    menu = '>>>>>>>> Celulares(s) Selecionado >>>>>>>>\n'
    menu += '1 - Mostrar detalhes do Celular\n'
    menu += '2 - Remover Celular\n'
    menu += '3 - Editar celular\n'
    menu += '4 - Duplicar celular\n'
    
    menu += 'opcao >>> '
    opcao_2 = int(input(menu))

    if opcao_2 ==  1:
        print(30*'>>>')
        print('Nome:', celulares[selecionado]['nome'])
        print('Marca:', celulares[selecionado]['marca'])
        print('Tela:', celulares[selecionado]['tela'])
        print('Valor:', celulares[selecionado]['valor'])
        print('Cam_frontal:', celulares[selecionado]['cam_frontal'])
        print(30*'>>>')

    elif opcao_2 == 2:
        del celulares[selecionado]
        print('Celular Removido com sucesso')

    elif opcao_2 == 3:
        menu_2 = '>>>>>>>> Editor de Informações >>>>>>>>\n'
        menu_2 += '1 - Editar Nome\n'
        menu_2 += '2 - Editar Marca\n'
        menu_2 += '3 - Editar Tela\n'
        menu_2 += '4 - Editar Valor\n'
        menu_2 += '5 - Editar Camera(Sim/Não)\n'
        menu_2 += '6 - Editar Todas as Informações\n'

        menu_2 += 'opcao >>> '
        opcao_3 = int(input(menu_2))

        if opcao_3 == 1 or opcao_3 == 6:
            celulares[selecionado]['nome'] = input('Digite o Novo nome do celular: ')
        if opcao_3 == 2 or opcao_3 == 6:
            celulares[selecionado]['marca'] = input('Digite a nova marca do celular: ')
        if opcao_3 == 3 or opcao_3 == 6:
            celulares[selecionado]['tela'] = input('Digite o novo tamanho de Tela do celular: ')
        if opcao_3 == 4 or opcao_3 == 6:
            celulares[selecionado]['valor'] = input('Digite o Novo Valor do celular(R$): ')
        if opcao_3 == 5 or opcao_3 == 6:
            celulares[selecionado]['cam_frontal'] = input('Digite se possui camera frontal(Sim/Não): ')

    elif opcao_2 == 4:
        celulares.append(celulares[selecionado])
main()