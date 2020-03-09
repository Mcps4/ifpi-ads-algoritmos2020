import turtle
import math
def square(t,length):
    for i in range(4):
        t.forward(length)
        t.lt(90)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,length,n):
    angle = 360.0 / n
    polyline(t,n,lenght,angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    # corretor de aproximação
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def circle(t, r):
    arc(t, r, 360)

def main():
    lince = turtle.Turtle()
    raio = 50
    lince.pu()
    lince.fd(raio)
    lince.lt(90)
    lince.pd()
    circle(lince, raio)

main()
turtle.mainloop()