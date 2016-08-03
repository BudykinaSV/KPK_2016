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

canvas=Tkinter.Canvas(root, background='green',width=400,height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

line=canvas.create_line(0,0,10,10)
for i in range(1,8,1):
    oval=canvas.create_oval(i*40,i*40,i*40+20,i*40+20,fill='white',width=2, outline="red")

root.mainloop()
print("Приложение завершило работу")