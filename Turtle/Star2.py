import turtle

t = turtle.Turtle()
t.speed(2)
t.fillcolor("yellow")
t.begin_fill()

points = [
    (0, 100),
    (23, 31),
    (95, 31),
    (38, -12),
    (59, -81),
    (0, -40),
    (-59, -81),
    (-38, -12),
    (-95, 31),
    (-23, 31)
]

t.penup()
t.goto(points[0])
t.pendown()

for p in points[1:]:
    t.goto(p)

t.goto(points[0])
t.end_fill()

t.hideturtle()
turtle.done()