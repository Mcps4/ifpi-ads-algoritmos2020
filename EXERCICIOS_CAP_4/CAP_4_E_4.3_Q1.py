import turtle
t = turtle.Turtle()
def square(t):
    for i in range(4):
        t.forward(100)
        t.lt(90)

def main():
    square(t)
    turtle.mainloop()
    
main()