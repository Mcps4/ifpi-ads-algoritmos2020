import turtle
t = turtle.Turtle()
def polygon(t,n,length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.lt(angle)

def main():     
    polygon(t,6,90)
    turtle.mainloop()

main()