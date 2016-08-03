#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter

def paint(event):
    print(event.x, event.y)
    if event.widget!=canvas:
        print('Странно. Событие привязано к canvas')
        return
    canvas.coords(line,0,0,event.x, event.y)

root=Tkinter.Tk()

canvas=Tkinter.Canvas(root)
canvas.bind("<Motion>", paint)
canvas.pack()

line=canvas.create_line(0,0,10,10)


root.mainloop()
print("Приложение завершило работу")