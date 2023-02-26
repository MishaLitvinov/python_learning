from tkinter import *
window=Tk()
window.geometry('1000x1000')
canv=Canvas(window,width=1000,
            height=1000, bg='light blue')
canv.place(x=0,y=0)

canv.create_oval([300,300], [700,700],
                 width=0, fill='Chocolate',outline='SaddleBrown')#head
canv.create_oval([550,300], [750,500],
                 width=0, fill='Chocolate',outline='SaddleBrown')#first ear
canv.create_oval([250,300], [450,500],
                 width=0, fill='Chocolate',outline='SaddleBrown')#second ear
canv.create_oval([400,400], [420,430],
                 width=1.5, fill='Blue',outline='Black')#first eye
canv.create_oval([580,400], [600,430],
                 width=1.5, fill='Blue',outline='Black')#second eye
canv.create_arc([400,475], [600,600],
                 extent=-180, style=ARC,width=3,outline='red')#mouth
canv.create_polygon(475, 475, 525, 475, 500, 525,\
        outline='Black', fill="SaddleBrown", width=3)#nose


def move_bear(event):
    if event.keysym == 'Up':
        canv.move(1, 0, -3)
    if event.keysym == 'Down':
        canv.move(1, 0, 3)
    if event.keysym == 'Left':
        canv.move(1, -3, 0)
    else:
        canv.move(1, 3, 0)

canv.bind_all('<KeyPress-Up>', move_bear)
canv.bind_all('<KeyPress-Down>', move_bear)
canv.bind_all('<KeyPress-Left>', move_bear)
canv.bind_all('<KeyPress-Right>', move_bear)
