def main():

    hora_1 = int(input('digite a hora do inicio do jogo: '))
    min_1 = int(input('digite os minutos de inicio do jogo: '))

    hora_2 = int(input('digite a hora do final do jogo: '))
    min_2 = int(input('digite os minutos do final do jogo: '))

    duracao(hora_1, min_1, hora_2, min_2)

def duracao(hora_1, min_1, hora_2, min_2):
    hora_in = hora_1 + min_1 / 60
    hora_fn = hora_2 + min_2 / 60
    duracao = hora_fn - hora_in
    tempo_neg = 24 + (hora_fn - hora_in)

    if hora_fn > hora_in:
        print(f'o jogo tem duração de {duracao} hora(s)')

    if hora_fn < hora_in:
        print(f'o jogo tem duração de {tempo_neg} hora(s)')

        
main()