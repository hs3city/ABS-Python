import turtle as trtl


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


def draw_window(x):
    draw_square(x)


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
draw_window(50)
bob.goto(200, 200)
draw_window(75)
bob.goto(100, 0)
draw_rectangle(100, 150)
bob.goto(0, 300)
draw_triangle(300, 50)


trtl.done()
