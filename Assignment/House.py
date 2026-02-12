
import turtle

def draw_square(t, side):
   for _ in range(4):
       t.forward(side)
       t.left(90)


def draw_triangle(t, side):
    for _ in range(3):
        t.forward(side)
        t.left(120)


def draw_house(t):
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    draw_square(t, 200)
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    draw_triangle(t, 200)


if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(1)

    draw_house(t)

    turtle.done()