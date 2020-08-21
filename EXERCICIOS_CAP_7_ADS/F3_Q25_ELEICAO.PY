def main():
    n = int(input('digite o numero de eleitores: '))
    cont = 1
    can_1 = 0
    can_2 = 0
    can_3 = 0
    nu  = 0 
    br = 0

    while cont <= n:
        voto  = int(input('digite o numero do candidado de sua preferencia: '))
        if voto == 1:
            can_1 += 1

        elif voto == 2:
            can_2 += 1

        elif voto == 3:
            can_3 += 1

        elif voto == 9:
            nu += 1
        
        elif voto == 0:
            br += 1

        else:
            print('desculpe seu voto e inválido')

        cont += 1

        if (can_1 > can_2) and (can_1 > can_3) and (can_1 != can_2) and (can_1 != can_3):
            print(f'\n o candidado 1 foi eleito com {can_1} votos')

        elif (can_2 > can_1) and (can_2 > can_3) and (can_2 != can_1) and (can_2 != can_3):
            print(f'\n o candidado 1 foi eleito com {can_2} votos')

        elif (can_3 > can_1) and (can_3 > can_2) and (can_3 != can_2) and (can_3 != can_1):
            print(f'\n o candidado 1 foi eleito com {can_3} votos')

        else:
            print('Houve empate entre alguns dos candidatos')

        print(">>" * 50)
        print(f"Candidato 1: {can_1}")
        print(f"Candidato 2: {can_2}")
        print(f"Candidato 3: {can_3}")
        print(f"Brancos: {br}")
        print(f"Nulos: {nu}")
        print(">>" * 50)

main()