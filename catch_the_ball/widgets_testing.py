#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter #подключение библиотеки

def button1_command():
    print('Enter tuknut')


def print_hello(event):
    print("Hello!")
    #print(event.char)
    #print(event.keycode)
    #print(event.num)
    print(event.x,event.y)
    #print(event.x_root,event.y_root)
    m1=event.widget
    print(m1)
    if m1==button1:
        print("button1")
    elif m1==button2:
        print("button2")
    else:
        print("error")
        #raise ValueError()


def init_main_window():
    global root, button1, button2, label, text, scale
    root=Tkinter.Tk()
    button1=Tkinter.Button(root,text='Button1',command=button1_command)
    button1.bind('<Button>',print_hello)
    button1.pack()
    button2=Tkinter.Button(root,text='Button2')
    button2.bind('<Button>',print_hello)
    button2.pack()

    variable=Tkinter.IntVar(0)
    label=Tkinter.Label(root,textvariable=variable)
    text=Tkinter.Entry(root, textvariable=variable)
    scale=Tkinter.Scale(root,orient=Tkinter.HORIZONTAL, length=300,
        from_=0, to=100, tickinterval=10, resolution=5, variable=variable)
    for obj in label,text,scale:
        obj.pack()



if __name__=="__main__":
    init_main_window()

root.mainloop()