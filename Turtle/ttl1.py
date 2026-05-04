import turtle

t = turtle.Turtle()
t.speed(5)

t.forward(100)    # line
t.penup()
t.goto(0, 50)     # move without drawing
t.pendown()
t.circle(40)      # draw circle