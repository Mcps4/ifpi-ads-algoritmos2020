import turtle
t = turtle.Turtle()
def square(t,length):
    for i in range(4):
        t.forward(length)
        t.lt(90)

def main():
    square(t,200)
    turtle.mainloop()
    
main()