#!/usr/bin/env python
# -*- coding: utf-8 -*-
from turtle import Turtle

def init_drawman():
    global x_current, y_current, t, _drawman_scale
    t=Turtle()
    t.penup()
    x_current=0
    y_current=0
    t.goto(x_current,y_current)
    _drawman_scale=10

def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale=scale

def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx,dy):
    to_point(x_current+dx,y_current+dy)

def to_point(x,y):
    global x_current,y_current
    x_current=x
    y_current=y
    t.goto(_drawman_scale*x_current,_drawman_scale*y_current)

def test_drawman():
    """  """
    pen_down()
    for i in range(5):
        on_vector(1,2)
        on_vector(1,-2)
    pen_up()
    to_point(0,0)

init_drawman()
if __name__=='__main__':
    import time
    test_drawman()
    time.sleep(10)
