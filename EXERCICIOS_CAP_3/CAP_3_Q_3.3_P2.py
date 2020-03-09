def do_twice(a):
    a()
    a()

def do_four(a):
    do_twice(a)
    do_twice(a)

def print_sinais():
    print(2 * '+ - - - -', end = ' ')

def print_down():
    print(2 * '|        ', end = ' ')

def print_mais():
    do_twice(print_sinais)
    print('+')

def print_barras():
    do_twice(print_down)
    print('|')

def print_linha():
    print_mais()
    do_four(print_barras)

def print_figura():
    do_four(print_linha)
    print_mais()

def main():
    print_figura()
main()

    