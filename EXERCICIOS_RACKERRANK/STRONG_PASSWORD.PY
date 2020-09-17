def main():
    password = input('Digite a senha: ')

    print(strong_password(password))



def strong_password(p):
    if maior_igual_6(p):
        requisitos = number(p) + minuscula(p) + maiuscula(p) + simbol(p)
        if requisitos == 4:
            return 'Senha válida'

        else:
            r = 4 - requisitos
            return r

    else:
        r = 6 - len(p)
        return r

def maior_igual_6(p):
    if len(p) >= 6:
        return True
    else:
        return False

def number(p):
    cont = 0
    for i in p:
        i = ord(i)
        if (i >= 48 and i <= 57):
            cont = 1
    return cont
        

def minuscula(p):
    cont = 0
    for i in p:
        i = ord(i)
        if (i >= 97 and i <= 122):
            cont = 1

    return cont


def maiuscula(p):
    cont = 0
    for i in p:
        i = ord(i)
        if (i >= 65 and i <= 90):
            cont = 1
    return cont
        
def simbol(p):
    cont = 0
    simbols = "!@#$%^&*()-+"
    for i in p:
        for c in simbols:
            if c == i:
                cont = 1
        return cont


main()