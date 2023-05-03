#Un fram es un contenedor rectangular para agrupar y contener widgets
from tkinter import *
window = Tk()

frame = Frame(window,bg='pink',relief=SUNKEN)
frame.place(x=40,y=90)

Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

window.mainloop()