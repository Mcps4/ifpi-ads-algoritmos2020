def main():
    num_hexadecimal(num_decimal(num_binario()))

def num_binario():
    num  = []
    for i in range(8):
        num.append(int(input('digite um numero binario de 8 bits: ')))
        print(num[i])
        if (num[i] == 0) or (num[i] == 1):
            print()
        else:
            print('numero invalido')
            break
    return num

def num_decimal(binario):
    decimal = 0
    j = 0
    for i in binario:
        decimal += i * (2 ** (len(binario) - (j+1)))
        j += 1
    print(decimal)
    return decimal

def num_hexadecimal(decimal):
    hexadecimal = []
    novo_numero = ''
    while decimal >= 16:
        hexadecimal.append(decimal % 16)
        decimal =  decimal // 16
    hexadecimal.append(decimal)
    hexadecimal.reverse()
    for i in hexadecimal:
        if i > 9:
            if i == 10:
                novo_numero += 'A'
            elif i == 11:
                novo_numero += 'B'
            elif i == 12:
                novo_numero += 'C'
            elif i == 13:
                novo_numero += 'D'
            elif i == 14:
                novo_numero += 'E'
            elif i == 15:
                novo_numero += 'F'
        else:
            novo_numero += str(i)
    print(novo_numero)
main()