import turtle

hex = turtle.Turtle()
hex.speed(5)

hex.pencolor("black")
hex.fillcolor("red")
hex.begin_fill()

for i in range(6):
    hex.forward(100)
    hex.right(60)

hex.end_fill()
hex.hideturtle()

turtle.done()