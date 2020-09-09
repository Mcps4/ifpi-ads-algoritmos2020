def main():
    n_linhas = int(input('quantidade de linhas: '))
    
    for _ in range(0, n_linhas):
        frase =  input('Digite a frase a ser criptografada: ')
        print(f'{passo_3(passo_2(passo_1(frase)))}')

def passo_1(string):
    palavra_1 = ""
    for i in string:
        n = ord(i)
        if letra(n):
            n = ord(i) + 3
            n = chr(n)
            palavra_1 += n
        else:
            n = chr(n)
            palavra_1 += n
    return palavra_1

def passo_2(texto):
    retorno = ""
    for i in range(len(texto)-1, -1, -1):
        retorno += texto[i]
    return retorno

def passo_3(texto):
    frase_3 = ""
    for i in range(len(texto)):
        n = ord(texto[i])
        if n != 240 and (i >= len(texto)//2):
            n = ord(texto[i]) - 1
            n = chr(n)
            frase_3 += n 
        else:
            n = chr(n)
            frase_3 += n
    return frase_3

def letra(n):
    if (n >= 65) and (n <= 90) or (n >= 97) and (n <= 122):
        return True
    else:
        return False

    
main()




