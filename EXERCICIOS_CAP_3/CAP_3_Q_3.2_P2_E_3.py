def do_twice(f,a):
    f(a)
    f(a) 
def print_spam(a):
    print(a)
    
def main():

    do_twice(print_spam,'a')

main()

# Esta função atribui o argumento a um parâmetro chamado bruce. Quando a função é chamada, ela exibe o valor do parâmetro (seja qual for) duas vezes.
