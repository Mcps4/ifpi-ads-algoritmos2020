def main():

    num = int(input('digite um numero menor que mil: '))

    cen_dez_uni(num)

def cen_dez_uni(num):

    unidade = (num // 1) % 10
    dezena = (num // 10) % 10
    centena = (num // 100) % 10

    if 100 <= num < 1000:
        print(f'o numero possui {centena} centenas, {dezena} dezenas e {unidade} unidades')

    elif 10 <= num < 100:
        print(f'o numero possui 0 centenas, {dezena} dezenas e {unidade} unidades')

    else:
        print(f'o numero possui 0 centenas, 0 dezenas e {unidade} unidades')

main()