import turtle 
import math

lince = turtle.Turtle()
lince.speed(10)
def polyline(t, n, length, angle):
    for i in range(n):
        t.bk(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def arco_curvo(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def main():
    cont = 0
    for i in range(10):
        arc(lince,100 , 45 - cont)
        lince.lt(cont)
        
        cont += 4
    turtle.mainloop()


lince.hideturtle()
main()