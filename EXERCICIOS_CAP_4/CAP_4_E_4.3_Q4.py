import turtle
import math
t = turtle.Turtle()
def polygon(t,length,n):
    angulo = 360.0 / n
    for i in range(n):
        t.forward(length)
        t.lt(angulo)

def circle(t,r):
    comprimento = (2 * math.pi * r) / 360
    polygon(t,comprimento,360)

def main():
    circle(t,50)
    turtle.mainloop()
    
main()