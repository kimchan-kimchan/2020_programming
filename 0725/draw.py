import turtle as t

draw_action = 1
oldx = 0
oldy = 0

def new_clear():
    global draw_action
    global oldx
    global oldy
    t.clear()
    t.color("black")
    t.pensize(1)
    t.pendown()
    draw_action = 1
    oldx = 0
    oldy = 0

def draw(x,y):
    global oldx
    global oldy
    deltax=x-oldx
    deltay=y-oldy

    if draw_action == 1:
        t.goto(x,y)
        oldx = x
        oldy = y
        
    elif draw_action == 2:
        t.goto(x,oldy)
        t.goto(x,y)
        t.goto(oldx,oldy)
        
    elif draw_action == 3:
        t.goto(x,oldy)
        t.goto(x,y)
        t.goto(oldx,y)
        t.goto(oldx,oldy)
        
    elif draw_action == 4:
        t.circle(-((x-oldx)//2))
        
    elif draw_action == 5:
        t.fillcolor("yellow")
        t.color("yellow")
        t.begin_fill()
        t.goto(x,y)
        t.goto(x-1.25*deltax,y)
        t.goto(oldx+0.75*deltax,oldy)
        t.goto(oldx+deltax*0.5,oldy+deltay*1.75)
        t.goto(oldx,oldy)
        t.end_fill()

        
    elif draw_action == 6:
        t.goto(x,oldy)
        t.goto(x,y)
        t.goto(oldx+0.15*deltax,y)
        t.goto(oldx+0.15*deltax,oldy+0.15*deltay)
        t.goto(oldx+0.85*deltax,oldy+0.15*deltay)
        t.goto(oldx+0.85*deltax,oldy+0.85*deltay)
        t.goto(oldx+0.3*deltax,oldy+0.85*deltay)
        t.goto(oldx+0.3*deltax,oldy+0.3*deltay)
        t.goto(oldx+0.7*deltax,oldy+0.3*deltay)
        t.goto(oldx+0.7*deltax,oldy+0.7*deltay)
        t.goto(oldx+0.45*deltax,oldy+0.7*deltay)
        t.goto(oldx+0.45*deltax,oldy+0.45*deltay)
        t.goto(oldx+0.55*deltax,oldy+0.45*deltay)

    elif draw_action == 7:
        for i in range(20):
            t.goto(oldx+deltax*0.05*(i+1),oldy+deltay*0.05*(i+1))
            t.pensize(i+1)
        t.pensize(1)
    
        


def drag(x,y):
    if draw_action == 1:
        draw(x,y)

def move(x,y):
    global oldx
    global oldy
    penstatus = t.isdown()
    t.penup()
    t.goto(x,y)
    if penstatus == 1:
        t.pendown()
    oldx = x
    oldy = y

def key_l():
    global draw_action
    draw_action = 1
def key_t():
    global draw_action
    draw_action = 2
def key_r():
    global draw_action
    draw_action = 3
def key_c():
    global draw_action
    draw_action = 4
def key_s():
    global draw_action
    draw_action = 5
def key_p():
    global draw_action
    draw_action = 6
def key_r():
    global draw_action
    draw_action = 7
def key_n():
    new_clear()
def key_u():
    t.penup()
def key_d():
    t.pendown()
def key_red():
    t.pendown()
    t.color("red")
def key_orange():
    t.color("orange")
def key_yellow():
    t.color("yellow")
def key_green():
    t.color("green")
def key_blue():
    t.color("blue")
def key_navy():
    t.color("navy")
def key_purple():
    t.color("purple")
def key_black():
    t.color("black")

t.setup(600,600)
s = t.Screen()
t.shapesize(2)
t.speed(0)
t.left(90)
new_clear()
t.ondrag(drag)
t.bgcolor("black")

s.onkey(key_l,"l")
s.onkey(key_t,"t")
s.onkey(key_r,"r")
s.onkey(key_c,"c")
s.onkey(key_s,"s")
s.onkey(key_p,"p")
s.onkey(key_r,"r")
s.onkey(key_red,"1")
s.onkey(key_orange,"2")
s.onkey(key_yellow,"3")
s.onkey(key_green,"4")
s.onkey(key_blue,"5")
s.onkey(key_navy,"6")
s.onkey(key_purple,"7")
s.onkey(key_black,"0")

s.onkey(key_n,"n")
s.onkey(key_u,"u")
s.onkey(key_d,"d")
s.onscreenclick(draw,1)
s.onscreenclick(move,3)
s.listen()
