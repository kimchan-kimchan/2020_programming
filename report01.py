import turtle as t
t.pensize(8)
r=55
d=123

t.color("purple")
t.circle(r)
t.penup()
t.forward(d)
t.pendown()

t.color("black")
t.circle(r)
t.penup()
t.forward(d)
t.pendown()

t.color("red")
t.circle(r)
t.penup()

t.right(180)
t.forward(2*d)
t.right(180)
t.forward(d/2)
t.right(90)
t.forward((d/2)-10)
t.left(90)
t.pendown()

t.color("yellow")
t.circle(r)
t.penup()
t.forward(d)
t.pendown()

t.color("green")
t.circle(r)
