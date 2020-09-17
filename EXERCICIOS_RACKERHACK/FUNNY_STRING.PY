def main():
    string = input('Digite a string que você quer ver se é funny: ')
    print(funnystring(string, reverse(string)))

def funnystring(s, r):
    if wrd(s) == reverse_wrd(r):
        return "Funny"

    else:
        return "Not Funny"
        

def wrd(s):
    word = ""
    antes = 0
    cont_1 = 1
    for i in s:
        atual = ord(i)
        if cont_1 > 1:
            word += str(atual - antes)

        antes = atual
        cont_1 += 1
    return word
        
    
def reverse_wrd(s):
    reverse_word = ""
    antes = 0 
    cont_2 = 1
    for l in s:
        atual = ord(l)
        if cont_2 > 1:
            reverse_word += str(antes - atual)
        antes = atual
        cont_2 += 1
    return reverse_word


def reverse(s):
    retorno = ''
    for i in range(len(s)-1, -1, -1):
        retorno += s[i]

    return retorno

main()
