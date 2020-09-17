def main():
    mensagem = input('Digite a messagem do robô: ')
    print(mars_exploration(mensagem))

def mars_exploration(m):
    cont = 1
    ac = 0
    for l in m:
        le  = ord(l)
        if cont > 3:
            cont = 1
        if letra_o(le,cont):
            ac = ac
        elif letra_s(le, cont):
            ac = ac
        else:
            ac += 1
        cont += 1
    return ac



def letra_o(le, cont):
    if (cont % 2 == 0) and (le == 79 or le == 111):
            return True
    else:
            return False
    

def letra_s(le,cont):
    if (cont % 2 != 0) and (le == 83 or le == 115):
            return True
    else:
        return False


main()