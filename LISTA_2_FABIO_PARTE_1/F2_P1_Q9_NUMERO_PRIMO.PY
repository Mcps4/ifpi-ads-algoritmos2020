def main():

    num = int(input('digite um numero entre 0 e 100: '))

    num_nao_primo(num)


def num_nao_primo(num):

    if (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0) and (num != 2 and num != 3 and num != 5 and num != 7) or num == 1:
        print('o numero não é primo')

    else:
        print('o numero é primo')

main()
