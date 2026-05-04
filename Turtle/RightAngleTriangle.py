import turtle, math

t = turtle.Turtle()
t.speed(2)

def triangle(a,b):
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(135)
    x = math.sqrt(a**2+b**2) #C2 = a2 + b2
    t.forward(x)
    turtle.done()

triangle(100, 100)