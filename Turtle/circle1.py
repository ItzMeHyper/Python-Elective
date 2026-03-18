import turtle 

cir = turtle.Turtle()

count = 0

cir.speed(500)
cir.fillcolor("blue")

cir.begin_fill()

while(count<360):
    cir.forward(2)
    cir.left(1)
    count = count + 1

cir.end_fill()
cir.hideturtle()

turtle.done()