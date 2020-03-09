def do_twice(f,spam):
    f(spam)
    f(spam) 
def print_spam(spam):
    print(spam)
def print_twice(spam):
    print(spam)
def main():
    do_twice(print_spam,'spam')
    do_twice(print_twice,'spam')


main()