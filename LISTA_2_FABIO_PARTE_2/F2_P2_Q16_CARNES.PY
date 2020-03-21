def main():
    tp_pagamento = str(input('digite a forma de pagamento: '))
    tp_carne = str(input('digite o tipo de carne que deseja: '))
    qtd_file = int(input('digite a quantidade em kilos de filé: '))
    qtd_alcatra = int(input('digite a quantidade em kilos de alcatra: '))
    qtd_picanha = int(input('digite a quantidade em kilos de picanha: '))

    valor_carnes(tp_pagamento, tp_carne, qtd_file, qtd_alcatra, qtd_picanha)
    
def valor_carnes(tp_pagamento, tp_carne, qtd_file, qtd_alcatra, qtd_picanha):

    F = 'file'
    A = 'alcatra'
    P = 'picanha'

    preco_file_1 = 4.9 * qtd_file
    preco_alcatra_1 = 5.9 * qtd_alcatra
    preco_picanha_1 = 6.9 * qtd_picanha
    preco_file_2 = 5.8 * qtd_file
    preco_alcatra_2 = 6.8 * qtd_alcatra
    preco_picanha_2 = 7.8 * qtd_picanha

    desconto_1 = (5 / 100) * preco_file_1 
    desconto_2 = (5 / 100) * preco_alcatra_1 
    desconto_3 = (5 / 100) * preco_picanha_1 
    desconto_4 = (5 / 100) * preco_file_2 
    desconto_5 = (5 / 100) * preco_alcatra_2
    desconto_6 = (5 / 100) * preco_picanha_2 

    valor_final_1 = preco_file_1 - desconto_1
    valor_final_2 = preco_alcatra_1 - desconto_2
    valor_final_3 = preco_picanha_1 - desconto_3
    valor_final_4 = preco_file_2 - desconto_4
    valor_final_5 = preco_alcatra_2 - desconto_5
    valor_final_6 = preco_picanha_2 - desconto_6

    if tp_pagamento == 'cartao':
        print('Seu tipo de pagamento é cartao!')
        print('Seu desconto é de 5 %')
    
        if tp_carne == F and qtd_file <= 5:
            print(f'o preço total é R${preco_file_1}')
            print(f'o valor a pagar é R${valor_final_1}')
            print(f'{qtd_file} kg de file')
        
        if tp_carne == F and qtd_file > 5:
            print(f'o preço total é R${preco_file_2}')
            print(f'o valor a pagar é R${valor_final_4}')
            print(f'{qtd_file} kg de file')
        
        if tp_carne == A and qtd_alcatra <= 5:
            print(f'o preço total é R${preco_alcatra_1}')
            print(f'o valor a pagar é R${valor_final_2}')
            print(f'{qtd_alcatra} kg de alcatra')
        
        if tp_carne == A and qtd_alcatra > 5:
            print(f'o preço total é R${preco_alcatra_2}')
            print(f'o valor a pagar é R${valor_final_5}')
            print(f'{qtd_alcatra} kg de alcatra')
        
        if tp_carne == P and qtd_picanha <= 5:
            print(f'o preço total é R${preco_picanha_1}')
            print(f'o valor a pagar é R${valor_final_3}')
            print(f'{qtd_picanha} kg de picanha')
        
        if tp_carne == P and qtd_picanha > 5:
            print(f'o preço total é R${preco_picanha_2}')
            print(f'o valor a pagar é R${valor_final_6}')
            print(f'{qtd_picanha} kg de picanha')
    
    else:
        print('Seu tipo de pagamento é em Dinheiro!')
    
        if tp_carne == F and qtd_file <= 5:
            print(f'o preço total é R${preco_file_1}')
            print(f'o valor a pagar é R${preco_file_1}')
            print(f'{qtd_file} kg de file')
        
        if tp_carne == F and qtd_file > 5:
            print(f'o preço total é R${preco_file_2}')
            print(f'o valor a pagar é R${preco_file_2}')
            print(f'{qtd_file} kg de file')
        
        if tp_carne == A and qtd_alcatra <= 5:
            print(f'o preço total é R${preco_alcatra_1}')
            print(f'o valor a pagar é R${preco_alcatra_1}')
            print(f'{qtd_alcatra} kg de alcatra')
        
        if tp_carne == A and qtd_alcatra > 5:
            print(f'o preço total é R${preco_alcatra_2}')
            print(f'o valor a pagar é R${preco_alcatra_2}')
            print(f'{qtd_alcatra} kg de alcatra')
        
        if tp_carne == P and qtd_picanha <= 5:
            print(f'o preço total é R${preco_picanha_1}')
            print(f'o valor a pagar é R${preco_picanha_1}')
            print(f'{qtd_picanha} kg de picanha')
        
        if tp_carne == P and qtd_picanha > 5:
            print(f'o preço total é R${preco_picanha_2}')
            print(f'o valor a pagar é R${preco_picanha_2}')
            print(f'{qtd_picanha} kg de picanha')
    
    print(f'o tipo de carne escolhido é {tp_carne}')


main()