#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
from random import choice, randint
from math import cos, sin, pi
import time
import signal

ball_initial_number=100
ball_maximal_radius=30
ball_minimal_radius=15
ball_available_colors=["lightgray","blue","red","#FFFF00","#FF00FF"]

def click_ball(event):
    """обработчик событий мыши, удаление шарика по клику мышкой
    вести счет кликнутых шариков
    """
    #event.x, event.y
    obj = canvas.find_closest(event.x, event.y)
    x1,y1,x2,y2=canvas.coords(obj)
    if x1<=event.x<=x2 and y1<=event.y<=y2:
        canvas.delete(obj)

def create_random_ball():
    """создание шарика с случайным размещением
    шарик не выходит за границы холста
    """
    R=randint(ball_minimal_radius,ball_maximal_radius)
    x=randint(0+R,int(canvas['width'])-1-2*R)
    y=randint(0+R,int(canvas['height'])-1-2*R)

    oval=canvas.create_oval(x,y,x+2*R,y+2*R,fill=random_color(),width=1, outline="red")


def random_color():
    """генератор случайных цветов шариков"""
    return choice(ball_available_colors)

def init_ball_catch_game():
    """
    Создает необходимое для игр количество шариков,
    по которым нужно кликать
    """
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root, canvas

    root=Tkinter.Tk()

    canvas=Tkinter.Canvas(root, background='green',width=400,height=400)
    canvas.bind("<Button>", click_ball)
    canvas.pack()


if __name__=="__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()