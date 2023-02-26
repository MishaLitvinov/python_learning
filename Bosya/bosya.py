from turtle import *
from playsound import playsound
#test commit

def oval(x_axis, y_axis, direction, start, end, fill):
    a=list(range(0,361))
    step = x_axis/100
    inc = (y_axis-x_axis)/10000
    for x in range(0,361):
        a[x]=step
        if(0<=x<90):step+=inc
        elif(90<=x<180):step+=-inc
        elif(180<=x<270):step+=inc
        elif(270<=x<360):step+=-inc
    
    if(direction=='left' or direction==False): left(start)
    else: right(start)
    if(fill):begin_fill()
    for x1 in range(start,end):
        forward(a[x1])
        if(direction=='left' or direction==False): left(1)
        else: right(1)
    if(fill):end_fill()
        

def playvoice(x,y):    
    playsound('03426.mp3')


reset()


onclick(playvoice)
speed(0)
tracer(10, 5)
color('black', 'white')

home()
oval(200,100,'left',0,360,0)

body_x = 40
body_w = 120
body_t = 250

up()
home()
goto(body_x,12)
down()
oval(body_w,250,'right',30,330,0)

up()
home()
oval(200,100,'left',0,130,0)
right(90)
down()
oval(70,40,'left',0,210,0)

up()
home()
right(180)
oval(200,100,'right',0,130,0)
left(90)
down()
oval(70,40,'right',0,210,0)

up()
home()
goto(body_x,12)
oval(body_w,250,'right',30,40,0)
left(90)
down()
oval(100,60,'right',0,220,0)

up()
home()
right(180)
goto(-body_x,12)
oval(body_w,250,'left',30,40,0)
right(90)
down()
oval(100,60,'left',0,220,0)

up()
home()
goto(body_x,12)
oval(body_w,250,'right',30,120,0)
left(70)
down()
oval(170,20,'right',0,187,0)

up()
home()
right(180)
goto(-body_x,12)
oval(body_w,250,'left',30,120,0)
right(70)
down()
oval(170,20,'left',0,187,0)

#Нос

up()
home()
goto(0,20)
down()
oval(90,40,'left',0,360,0)

color('black', 'black')

up()
home()
goto(0,50)
down()
oval(30,10,'left',0,360,1)


#Глаза

eye_x = 40
eye_y = 80
eye_z = 10

color('black', 'black')

up()
home()
goto(eye_x,eye_y)
down()
oval(eye_z,eye_z,'left',0,360,1)

up()
home()
goto(-eye_x,eye_y)
down()
oval(eye_z,eye_z,'left',0,360,1)

tracer(1, 5)
up()
goto(0,65)
down()


done()


    
