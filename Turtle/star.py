import turtle

star = turtle.Turtle()
star.speed(5)

star.color("blue")

for i in range(5) :
    star.forward(100)
    star.left(144)
    
star.hideturtle()
turtle.done()