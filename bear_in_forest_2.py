import time

from tkinter import *
window = Tk()
window.geometry('2000x1000')
canv=Canvas(window,width=2000,
            height=1000, bg='light blue')
canv.place(x = 0, y=0)

step=30

class animals:
    def __init__ (self, name, color_head, color_eyes, color_nose, color_mouth):
        self.name = name
        self.color_head = color_head
        self.color_eyes = color_eyes 
        self.color_nose = color_nose
        self.color_mouth = color_mouth
        self.draw_parts = [] 

    def move(self, x, y):
        for part in self.draw_parts:
                canv.move(part, x, y)

class bear(animals):

    def draw(self):
        self.draw_parts.append (canv.create_oval(300,300, 700,700,
                        width=0, fill= self.color_head))
        self.draw_parts.append(canv.create_oval(550,300, 750,500,
                        width=0, fill=self.color_head))
        self.draw_parts.append(canv.create_oval(250,300, 450,500,
                        width=0, fill=self.color_head))
        self.draw_parts.append(canv.create_oval(400,400, 420,430,
                        width=1.5, fill=self.color_eyes,outline='Black'))
        self.draw_parts.append(canv.create_oval(580,400, 600,430,
                        width=1.5, fill=self.color_eyes,outline='Black'))
        self.draw_parts.append(canv.create_arc(400,475, 600,600,
                        extent=-180, style=ARC,width=3,outline=self.color_mouth))
        self.draw_parts.append(canv.create_polygon(475, 475, 525, 475, 500, 525,\
                outline='Black', fill=self.color_nose, width=2))


class rabits(animals):

    def draw(self):
        self.draw_parts.append (canv.create_oval(300,300, 700,700,
                        width=0, fill= self.color_head))
        self.draw_parts.append(canv.create_oval(550,50, 700,500,
                        width=0, fill=self.color_head))
        self.draw_parts.append(canv.create_oval(300,50, 450,500,
                        width=0, fill=self.color_head))
        self.draw_parts.append(canv.create_oval(400,400, 420,430,
                        width=1.5, fill=self.color_eyes,outline='Black'))
        self.draw_parts.append(canv.create_oval(580,400, 600,430,
                        width=1.5, fill=self.color_eyes,outline='Black'))
        self.draw_parts.append(canv.create_arc(400,475, 600,600,
                        extent=-180, style=ARC,width=3,outline=self.color_mouth))
        self.draw_parts.append(canv.create_polygon(475, 475, 525, 475, 500, 525,\
                outline='Black', fill=self.color_nose, width=2))
       
   
        
    
potapik = bear('Potapik','Chocolate','Blue','SaddleBrown','Red')
potapik.draw()

obnimaha = bear('Obnimaha','SaddleBrown','MediumSpringGreen','Black','Red')
obnimaha.draw()

mordastik = bear('Mordastik','Sienna','DarkTurquoise','SaddleBrown','DarkRed')
mordastik.draw()

bosya = bear('Bosya','Silver','Aquamarine','Black','Maroon')
bosya.draw()

kabasya = rabits('Kabasya','Silver','Aquamarine','Black','Maroon')
kabasya.draw()


def move_bear(event):
    match event.keysym:
        case 'Up':
            potapik.move(0, -step)
        case 'Down':
            potapik.move(0, step)
        case 'Left':
            potapik.move(-step, 0)
        case 'Right':
            potapik.move(step, 0)
        case 'x':
            obnimaha.move(step, 0)
        case 'z':
            obnimaha.move(-step, 0)
        case 'w':
            bosya.move(step,0 )
        case 's':
            bosya.move(-step, 0)
        case 'y':
            mordastik.move(step,0 )
        case 't':
            mordastik.move(-step, 0)
  

canv.bind_all('<KeyPress-Up>', move_bear)
canv.bind_all('<KeyPress-Down>', move_bear)
canv.bind_all('<KeyPress-Left>', move_bear)
canv.bind_all('<KeyPress-Right>', move_bear)
canv.bind_all('<KeyPress-x>', move_bear)
canv.bind_all('<KeyPress-z>', move_bear)
canv.bind_all('<KeyPress-w>', move_bear)
canv.bind_all('<KeyPress-s>', move_bear)
canv.bind_all('<KeyPress-t>', move_bear)
canv.bind_all('<KeyPress-y>', move_bear)

window.mainloop()