def main():
    tp_combustivel = str(input('digite o tipo de combustível: '))
    litros = float(input('digite o quantidade de litros: '))

    valor_combustivel(tp_combustivel, litros)
    
def valor_combustivel(tp_combustivel, litros):

    G = 'gasolina'
    A = 'álcool'

    preco_G = 2.5 * litros
    preco_A = 1.9 * litros

    desconto_G1 = (4 / 100) * preco_G
    desconto_G2 = (6 / 100) * preco_G
    desconto_A1 = (3 / 100) * preco_A
    desconto_A2 = (5 / 100) * preco_A

    preco_final_G1 = preco_G - desconto_G1
    preco_final_G2 = preco_G - desconto_G2
    preco_final_A1 = preco_A - desconto_A1
    preco_final_A2 = preco_A - desconto_A2

    if tp_combustivel == G and litros <= 20:
        print(f'o preço final é R$ {preco_final_G1}')

    elif tp_combustivel == G and litros > 20:
        print(f'o preço final é R$ {preco_final_G2}')

    elif tp_combustivel == A and litros <= 20:
        print(f'o preço final é R$ {preco_final_A1}')

    elif tp_combustivel == A and litros > 20:
        print(f'o preço final é R$ {preco_final_A2}')

main()