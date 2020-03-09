def do_twice(f,spam):
    f(spam)
    f(spam) 
def print_spam(spam):
    print(spam)
def print_twice(spam):
    print(spam)
def do_four(s,sit):
    s(print_spam,sit)
    s(print_spam,sit)
def main():
    do_twice(print_spam,'spam')
    do_twice(print_twice,'spam')
    do_four(do_twice,'al')


main()