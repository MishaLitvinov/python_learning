import turtle
t = turtle.Pen()
t.reset()
t.color('green')
t.begin_fill()
t.circle(100)
t.end_fill()
t.left(90)
t.up()
t.forward(150)
t.right(90)
t.backward(50)
t.left(90)
t.backward(50)
t.right(90)
t.backward(20)
t.down()
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.forward(140)
t.down()
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.backward(78)
t.down()
t.color('black')
t.begin_fill()
t.forward(20)
t.right(130)
t.forward(20)
t.right(100)
t.forward(20)
t.right(130)
t.forward(6)
t.end_fill()
t.up()
t.forward(8)
t.right(90)
t.forward(60)
t.right(90)
t.color('red')
for x in range(1, 51):
    t.forward(1)
    t.right(1)
t.down()
for x in range(1, 101):
    t.backward(1)
    t.left(1)
t.up()
for x in range(1, 51):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(60)
t.right(45)
t.forward(50)
t.left(45)
t.color('blue')
t.down()
t.begin_fill()
t.circle(5)
t.end_fill()
t.up()
t.left(90)
t.forward(70)
t.right(90)
t.down()
t.begin_fill()
t.circle(5)
t.end_fill()
t.up()
t.backward(100)
t.left(90)
t.forward(100)
t.left(180)
t.down()
def my_figure_1(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.left(120)
    t.forward(140)
    t.left(120)
    t.forward(140)
    t.left(120)
    t.forward(140)
    t.backward(70)
    t.end_fill()
    t.up()
    t.right(90)
    t.backward(60)
    t.left(90)
    t.down()
    t.begin_fill()
    t.left(240)
    t.forward(180)
    t.left(120)
    t.forward(180)
    t.left(120)
    t.forward(180)
    t.end_fill()
    t.up()
    t.right(30)
    t.backward(156)
    t.right(90)
    t.forward(20)
    t.color(0.5, 0, 0)
    t.down()
    t.begin_fill()
    for x in range(1, 3):
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(40)
    t.end_fill()
my_figure_1(0, 0.5, 0)

