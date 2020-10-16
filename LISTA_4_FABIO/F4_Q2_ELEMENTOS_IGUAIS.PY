def main():
   print(elemento_igual())
    
def elemento_igual():
    a = []
    n = int(input('digite a quantidade de elementos: '))
    for i in range(n):
        a.append(int(input('Digite o valor que você quer adicionar no vetor: ')))

    if len(a) == 1:
        return 'Tamanho do vetor é insuficinete para comparação'
    elif len(a) == 2:
        if a[0] == a[1]:
            return 'No vetor inserido existem valores iguais'
    elif len(a) >= 3:
        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                if a[i] == a[j]:
                    return 'No vetor inserido existem valores iguais'


main()