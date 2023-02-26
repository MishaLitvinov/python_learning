from tkinter import *

window=Tk()
window.geometry('2000x1000')
canv=Canvas(window,width=2000,
            height=1000, bg='light blue')
canv.place(x=0,y=0)

class bear:

    def __init__(self, name, body_color):
        self.name = name
        self.draw_parts = []
        self.body_color = body_color
        self.size = 100
    

    def draw(self):
        self.draw_parts.append(canv.create_oval(300, 300, 700, 700, width=0, fill=self.body_color,outline='SaddleBrown'))
        self.draw_parts.append(canv.create_oval(550, 300, 750, 500, width=0, fill=self.body_color,outline='SaddleBrown'))
        self.draw_parts.append(canv.create_oval(250, 300, 450, 500,
                        width=0, fill=self.body_color,outline='SaddleBrown'))
        self.draw_parts.append(canv.create_oval(250, 600, 750, 1200,
                        width=0, fill=self.body_color,outline='Black'))
        self.draw_parts.append(canv.create_oval(400, 400, 420, 430,
                        width=1.5, fill='Blue',outline='Black'))
        self.draw_parts.append(canv.create_oval(580, 400, 600, 430,
                        width=1.5, fill='Blue',outline='Black'))
        self.draw_parts.append(canv.create_arc(400, 475, 600, 600,
                        extent=-180, style=ARC,width=3,outline='red'))
        self.draw_parts.append(canv.create_polygon(475, 475, 525, 475, 500, 525,
                        outline='Black', fill="SaddleBrown", width=3))


    def move(self, x, y):
        for part in self.draw_parts:
            canv.move(part, x, y)


potapik = bear('Potapik','Chocolate')
potapik.draw()

obnimaha = bear('Obnimaha','SaddleBrown')
obnimaha.draw()

mordastik = bear('Mordastik','Brown')
mordastik.draw()

bosya = bear('Bosya','White')
bosya.draw()

step = 30
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
            bosya.move(0, step)
        case 's':
            bosya.move(0, -step)


            
canv.bind_all('<KeyPress-Up>', move_bear)
canv.bind_all('<KeyPress-Down>', move_bear)
canv.bind_all('<KeyPress-Left>', move_bear)
canv.bind_all('<KeyPress-Right>', move_bear)
canv.bind_all('<KeyPress-x>', move_bear)
canv.bind_all('<KeyPress-z>', move_bear)
canv.bind_all('<KeyPress-w>', move_bear)
canv.bind_all('<KeyPress-s>', move_bear)

window.mainloop()