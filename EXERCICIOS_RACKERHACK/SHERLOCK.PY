def main():
    string = input('Digite  o anagrama: ')
    print(f'>>>> {anagramas(string)}')


def anagramas(s):
    ac = 0
    for i in range(0, len(s), 1):
        for j in range (i+1, len(s), 1):
            if palavra_1_letra(s)[i] == palavra_1_letra(s)[j]:
                ac += 1
    
    for i in range(0, len(s)-1, 1):
        for j in range (i+1, len(s)-1, 1):
            if palavras__2_letras(s)[i] == palavras__2_letras(s)[j]:
               ac += 1
    
    for i in range(0, len(s)-2, 1):
        for j in range (i+1, len(s)-2, 1):
            if palavra_3_letras(s)[i] == palavra_3_letras(s)[j]:
               ac += 1
    return ac


def palavra_1_letra(s):
    letras = []
    for i in s:
        letras.append(i)
    return letras

def palavras__2_letras(s):
    letras_2 = []
    for i in range(0, len(s)-1, 1):
        letras_2.append(ord(s[i])+ord(s[i+1]))
    return letras_2

def palavra_3_letras(s):
    letras_3 = []
    for i in range(0, len(s)-2, 1):
        letras_3.append(ord(s[i])+ord(s[i+1])+ord(s[i+2]))
    return letras_3


main()