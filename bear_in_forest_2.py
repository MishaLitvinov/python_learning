from tkinter import *

window=Tk()
window.geometry('1000x1000')
canv=Canvas(window,width=1000,
            height=1000, bg='light blue')
canv.place(x=0,y=0)

class bear:
    color = 'Chocolate'

    draw = [];
    def draw_bear(self):
        self.draw.append(canv.create_oval(300, 300, 700, 700,
                                                            width=0, fill='Chocolate',outline='SaddleBrown'))
        self.draw.append(canv.create_oval(550,300, 750,500,
                        width=0, fill='Chocolate',outline='SaddleBrown'))
        self.draw.append(canv.create_oval(250, 300, 450, 500,
                        width=0, fill='Chocolate',outline='SaddleBrown'))
        self.draw.append(canv.create_oval(250, 600, 750, 1200,
                        width=0, fill='Chocolate',outline='Black'))
        self.draw.append(canv.create_oval(400, 400, 420, 430,
                        width=1.5, fill='Blue',outline='Black'))
        self.draw.append(canv.create_oval(580, 400, 600, 430,
                        width=1.5, fill='Blue',outline='Black'))
        self.draw.append(canv.create_arc(400, 475, 600, 600,
                        extent=-180, style=ARC,width=3,outline='red'))
        self.draw.append(canv.create_polygon(475, 475, 525, 475, 500, 525,
                        outline='Black', fill="SaddleBrown", width=3))


    def move(self, x, y):
        for part in self.draw:
            canv.move(part, x, y)


potapik = bear()
potapik.draw_bear()

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

            
    

canv.bind_all('<KeyPress-Up>', move_bear)
canv.bind_all('<KeyPress-Down>', move_bear)
canv.bind_all('<KeyPress-Left>', move_bear)
canv.bind_all('<KeyPress-Right>', move_bear)


window.mainloop()