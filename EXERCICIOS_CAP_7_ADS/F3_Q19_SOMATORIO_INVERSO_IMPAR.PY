def main ():
    n = int(input('digite o valor de n: '))
    num = 1
    so = 0

    while n >= 1:
        if num % 2 != 0:
            so += num / n
        else:
            so -= n / num
        n -= 1
        num += 1

    print(f'o valor de S é: {so}')

main()