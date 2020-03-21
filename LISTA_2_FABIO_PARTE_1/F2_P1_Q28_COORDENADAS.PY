def main():

    x = float(input('Digite a coordenada das abscissa: '))
    y = float(input('Digite a coordenada das ordenadas: '))

    coordenadas(x, y)

def coordenadas(x, y):
    area = x * y
    area_2 = - area 

    if x < 0 and y < 0:
        print(f'A area do retangulo é: {area}')

    if x > 0 and y > 0:
        print(f'A area do retangulo é: {area}')

    if x > 0 and y < 0:
        print(f'A area do retangulo é: {area_2}')

    if x < 0 and y > 0:
        print(f'A area do retangulo é: {area_2}')

main()