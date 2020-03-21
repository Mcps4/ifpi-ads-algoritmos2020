def main():
    dia_at = int(input('digite o dia atual: '))
    mes_at = int(input('digite o numero do mes atual: '))
    ano_at = int(input('digite o ano atual: '))

    dia_sp = int(input('digite o dia de nascimento: '))
    mes_sp = int(input('digite o numero do mes de nascimento: '))
    ano_sp = int(input('digite o ano de nascimento: '))

    idade_exata(dia_at, mes_at, ano_at, dia_sp, mes_sp, ano_sp)

def idade_exata(dia_at, mes_at, ano_at, dia_sp, mes_sp, ano_sp ):

    idade_estimada = ano_at - ano_sp
    
    if mes_at < mes_sp:
        print(f'sua idade é de {idade_estimada - 1} anos')
    elif mes_at > mes_sp:
        print(f'sua idade é de {idade_estimada} anos')
    else:
        if dia_at < dia_sp:
            print(f'sua idade é de {idade_estimada - 1} anos')

        elif dia_at > dia_sp:
            print(f'sua idade é de {idade_estimada} anos')

main()
