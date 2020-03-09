import turtle
import math
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    # corretor de aproximação
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def petala(t, r,angle):
    for i in range(2):
        arc(t,r,angle)
        t.lt(180 - angle)

def flor(t,n,r,angle):
    for i in range(n):
        petala(t,r,angle)
        t.lt(360.0 / n)

def direcao(t, length):
    t.pu()
    t.fd(length)
    t.pd()

def main():
    lince = turtle.Turtle()
    direcao(lince,-100)
    flor(lince,7, 60.0, 60.0)

    direcao(lince, 100)
    flor(lince, 10, 40.0, 80.0)

    direcao(lince, 100)
    flor(lince, 20, 140.0, 20.0)
    
    lince.hideturtle()   

main() 
turtle.mainloop()
