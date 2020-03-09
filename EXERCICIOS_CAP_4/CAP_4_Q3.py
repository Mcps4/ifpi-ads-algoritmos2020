import math
import turtle
def torta(t, n, r):
    conjunto(t, n, r)
    t.pu()
    t.fd(r * 2 + 10)
    t.pd()

def conjunto(t,n,r):
    angulo = 360.0 / n
    for i in range(n):
        iso(t, r, angulo / 2 ) # triangulo de formaçao das tortas
        t.lt(angulo)

def iso(t, r, angulo):
    k = r * math.sin(angulo * math.pi / 180)

    t.rt(angulo)
    t.fd(r)
    t.lt(90 + angulo)
    t.fd(2 * k)
    t.lt(90 + angulo)
    t.fd(r)
    t.lt(180 - angulo)

def main():
    lince = turtle.Turtle()

    lince.pu()
    lince.bk(110)
    lince.pd()

    dimensao = 60
    torta(lince,5,dimensao)
    torta(lince,6,dimensao)
    torta(lince,7,dimensao)
    
    lince.hideturtle()

main()
turtle.mainloop()
