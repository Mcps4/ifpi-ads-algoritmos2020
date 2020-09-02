def main():
    string = str(input('digite a palavra ou letra que você quer ter rotacionada: '))
    numero  = int(input('digite o numero de rotação: '))

    rotate_word(numero, string)

def rotate_word(num, string):
        for i in string:
            n = ord(i)
            n = n + num
            print(chr(n), end="")



main()