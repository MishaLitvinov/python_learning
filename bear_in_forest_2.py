from tkinter import *

window=Tk()
window.geometry('1000x1000')
canv=Canvas(window,width=1000,
            height=1000, bg='light blue')
canv.place(x=0,y=0)

head = canv.create_oval(300,300, 700,700,
                 width=0, fill='Chocolate',outline='SaddleBrown')
first_ear = canv.create_oval(550,300, 750,500,
                 width=0, fill='Chocolate',outline='SaddleBrown')
second_ear = canv.create_oval(250,300, 450,500,
                 width=0, fill='Chocolate',outline='SaddleBrown')
first_eye=canv.create_oval(400,400, 420,430,
                 width=1.5, fill='Blue',outline='Black')
second_eye=canv.create_oval(580,400, 600,430,
                 width=1.5, fill='Blue',outline='Black')
mouth=canv.create_arc(400,475, 600,600,
                 extent=-180, style=ARC,width=3,outline='red')
nose=canv.create_polygon(475, 475, 525, 475, 500, 525,\
        outline='Black', fill="SaddleBrown", width=3)

def move_bear_parts(x, y):
    canv.move(head, x, y)
    canv.move(first_ear, x, y)
    canv.move(second_ear, x, y)
    canv.move(first_eye, x, y)
    canv.move(second_eye, x, y)
    canv.move(mouth, x, y)
    canv.move(nose, x, y)

step=30

def move_bear(event):
    match event.keysym:
        case 'Up':
            move_bear_parts(0, -step )
        case 'Down':
            move_bear_parts(0, step )
        case 'Left':
            move_bear_parts(-step, 0 )
        case 'Right':
            move_bear_parts(step, 0 )

            
    

canv.bind_all('<KeyPress-Up>', move_bear)
canv.bind_all('<KeyPress-Down>', move_bear)
canv.bind_all('<KeyPress-Left>', move_bear)
canv.bind_all('<KeyPress-Right>', move_bear)


window.mainloop()