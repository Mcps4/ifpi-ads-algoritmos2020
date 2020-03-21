def main():
    qtd_morangos = int(input('digite a quantidade em kilos de morangos: '))
    qtd_macas = int(input('digite a quantidade em kilos de maçãs: '))

    frutas(qtd_morangos, qtd_macas)

def frutas(qtd_morangos, qtd_macas):

    preco_morango_1 =  2.5 * qtd_morangos
    preco_macas_1 = 1.8 * qtd_macas
    preco_morango_2 =  2.2 * qtd_morangos
    preco_macas_2 = 1.5 * qtd_macas

    valor_total_1 = preco_morango_1 + preco_macas_1
    valor_total_2 = preco_morango_2 + preco_macas_2
    valor_total_3 = preco_morango_1 + preco_macas_2
    valor_total_4 = preco_morango_2 + preco_macas_1

    desconto_1 = (10 / 100) * valor_total_1
    desconto_2 = (10 / 100) * valor_total_2
    desconto_3 = (10 / 100) * valor_total_3
    desconto_4 = (10 / 100) * valor_total_4

    valor_final_1 = valor_total_1 - desconto_1
    valor_final_2 = valor_total_2 - desconto_2
    valor_final_3 = valor_total_3 - desconto_3
    valor_final_4 = valor_total_4 - desconto_4

    qtd_frutas = qtd_morangos + qtd_macas

    if qtd_frutas > 8 and qtd_morangos <= 5 and qtd_macas <= 5:
        print(f'O preço total é: {valor_final_1} R$')

    elif qtd_frutas > 8 or valor_total_2 > 25 and qtd_morangos > 5 and qtd_macas > 5:
        print(f'O preço total é: {valor_final_2} R$')

    elif qtd_frutas > 8 or valor_total_3 > 25 and qtd_morangos <= 5 and qtd_macas > 5:
        print(f'O preço total é: {valor_final_3} R$')

    elif qtd_frutas > 8 or valor_total_4 > 25 and qtd_morangos > 5 and qtd_macas <= 5:
        print(f'O preço total é: {valor_final_4} R$')

    elif qtd_morangos <= 5 and qtd_macas <= 5:
        print(f'O preço total é: {valor_total_1} R$')

    elif qtd_morangos <= 5 and qtd_macas > 5:
        print(f'O preço total é: {valor_total_3} R$')

    elif qtd_morangos > 5 and qtd_macas <= 5:
        print(f'O preço total é: {valor_total_4} R$')

main()