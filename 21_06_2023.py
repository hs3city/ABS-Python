import turtle as trtl

class Shape:
    CIRCLE = 'circle'
    SQUARE = 'square'

def draw_rectangle(x, y):
    bob.pendown()
    bob.forward(x)
    bob.left(90)
    bob.forward(y)
    bob.left(90)
    bob.forward(x)
    bob.left(90)
    bob.forward(y)
    bob.penup()
    bob.home()


def draw_square(x):
    bob.pendown()
    bob.forward(x)
    bob.left(90)
    bob.forward(x)
    bob.left(90)
    bob.forward(x)
    bob.left(90)
    bob.forward(x)
    bob.penup()
    bob.home()


def draw_window(x, shape):
    bob.pendown()
    if shape == Shape.SQUARE:
        draw_square(x)
    elif shape == Shape.CIRCLE:
        bob.circle(x)
        bob.penup()
        bob.home()
    else:
        print(f'Wrong shape: {shape}')


def draw_triangle(a, h):
    bob.pendown()
    x, y = bob.pos()
    bob.goto(x + a, y)
    bob.goto(x + a/2, y+h)
    bob.goto(x, y)
    bob.penup()
    bob.home()


bob = trtl.Turtle()
bob.speed(10)

draw_square(300)
bob.goto(50, 200)
draw_window(50, Shape.CIRCLE)
bob.goto(200, 200)
draw_window(75, Shape.SQUARE)
bob.goto(100, 0)
draw_rectangle(100, 150)
bob.goto(0, 300)
draw_triangle(300, 50)



trtl.done()
