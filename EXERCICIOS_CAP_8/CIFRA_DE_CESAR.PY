def main():
    string = str(input('digite a palavra ou letra que você quer ter rotacionada: '))
    numero  = int(input('digite o numero de rotação: '))

    rotate_word(numero, string)

def rotate_word(num, string):
        for i in string:
            n = ord(i)
            
            if (n >= 65) and (n <= 90):
                n = n + num

                if n <= 90:
                    print(chr(n), end="")

                elif n > 90:
                    n = (n - 90) + 64
                    print(chr(n), end="")

            elif (n >= 97) and (n <= 122):
                    n = n + num

                    if n <= 122:
                        print(chr(n), end="")

                    elif n > 122:
                        n = (n - 122) + 96
                        print(chr(n), end="")
        print()



main()