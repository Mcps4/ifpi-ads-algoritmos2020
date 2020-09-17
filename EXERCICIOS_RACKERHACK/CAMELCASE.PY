def main():
    s = input('digite a palavra: ')

    print(f'>>>> {camelcase(s)} palavras')

def camelcase(s):
    cont = 1
    for i in s:
        n = ord(i)
        if maiuscula(n):
            cont += 1

    return cont



def maiuscula(n):
    if (n >= 65 and n <= 90):
        return True

    else:
        return False



main()