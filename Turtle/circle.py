import turtle

circle = turtle.Turtle()

circle.speed(5)
circle.pencolor("black")
circle.fillcolor("green")

circle.begin_fill()

circle.circle(100)

circle.end_fill()
circle.hideturtle()
turtle.done()