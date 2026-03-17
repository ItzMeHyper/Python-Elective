import turtle

t = turtle.Turtle()

# square
for i in range(4):
    t.forward(100)
    t.left(90)

# hexagon
for i in range(6):
    t.forward(100)
    t.left(60)

turtle.done()