def main():

    dia_at = int(input('digite o dia atual: '))
    mes_at = int(input('digite o numero do mes atual: '))
    ano_at = int(input('digite o ano atual: '))

    dia_sp = int(input('digite o dia de nascimento: '))
    mes_sp = int(input('digite o numero do mes de nascimento: '))
    ano_sp = int(input('digite o ano de nascimento: '))

    idade_pessoa(dia_at, mes_at, ano_at, dia_sp, mes_sp, ano_sp)

def idade_pessoa(dia_at, mes_at, ano_at, dia_sp, mes_sp, ano_sp):

    qtd_anos = ano_sp - ano_at
       
    if (mes_at == mes_sp):
        
        if (dia_at > dia_sp):

            qtd_meses = qtd_anos * 12
            qtd_dias = qtd_anos * 360
            print(f'A quantidade em anos é de {qtd_anos} anos')
            print(f'A quantidade em meses é de {qtd_meses} meses')
            print(f'A quantidadade em dias é de {qtd_dias} dias')
    
    elif (mes_at > mes_sp):

        qtd_meses = qtd_anos * 12
        qtd_dias = qtd_anos * 360

        print(f'A quantidade em anos é de {qtd_anos} anos')
        print(f'A quantidade em meses é de {qtd_meses} meses')
        print(f'A quantidadade em dias é de {qtd_dias} dias')

    else:
        qtd_anos = (ano_at - ano_sp) 
        qtd_meses = qtd_anos * 12
        qtd_dias = qtd_anos * 360

        print(f'A quantidade em anos é de {qtd_anos} anos')
        print(f'A quantidade em meses é de {qtd_meses} meses')
        print(f'A quantidadade em dias é de {qtd_dias} dias')

main()