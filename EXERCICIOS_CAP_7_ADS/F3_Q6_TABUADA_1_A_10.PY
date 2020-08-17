def main():
    i = 1

    print('1 - adição , 2  - subtração, 3 - multiplicação, 4 - divisão ')

    t = int(input('digite a operação matematica que deseja: '))
    n = int(input('digite o numero que você quer saber a tabuada: '))

    while i <= 10: 
        if t == 1:
            tab = n + i
            print(f'{n} + {i}  = {tab}')
            i = i + 1


        elif t == 2:

            tab  = n - 1
            print(f'{n} - {i} = {tab}')
            i = i + 1

        elif t == 3:
            tab  = n * i
            print(f'{n} x {i} = {tab}')
            i = i + 1


        elif t == 4:
            tab  = n / i
            print(f'{n} / {i} = {tab}')
            i = i + 1


        else:
            print('numero invalido')
        

        

        


        

        

        

       
main()