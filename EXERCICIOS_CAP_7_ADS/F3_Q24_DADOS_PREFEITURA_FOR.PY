def main():
    n = int(input('digite a quantidade de habitantes: '))
    cont = 1
    pr = 0
    fi_t = 0
    sa_t = 0

    for cont in range(1,n + 1,1):
        sa = int(input('digite o salário: '))
        sa_t += sa

        if sa <= 1000:
            pr += 1

        fi = int(input('digite o numero de filhos: '))
        fi_t += fi
        

    
    print('>>' * 50)
    print(f' a media do salario da população é: {sa_t / n} ')
    print(f' a media de filhos por habitante é: {fi_t / n} ')
    print(f' percentual de pessoas com salario de até R$ 1000: {(100 * pr) / n} %')
    print('>>' * 50)
        
main()