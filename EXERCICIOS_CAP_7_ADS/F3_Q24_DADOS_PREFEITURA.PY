def main():
    n = int(input('digite a quantidade de habitantes: '))
    cont = 1
    pr = 0
    fi_t = 0
    sa_t = 0

    while cont <= n:
        sa = int(input('digite o salário: '))
        sa_t += sa

        if sa <= 1000:
            pr += 1

        fi = int(input('digite o numero de filhos: '))
        fi_t += fi
        cont += 1

    
    print('>>' * 50)
    print(f' a media do salario da população é: {sa_t / n} ')
    print(f' a media de filhos por habitante é: {fi_t / n} ')
    print(f' percentual de pessoas com salario de até R$ 1000: {(100 * pr) / n} %')
    print('>>' * 50)
        
main()