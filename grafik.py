#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proba import *
from time import sleep

def f(x):
    return x**2

drawman_scale(10)
"""обращение к функции модуля proba.ry
   с параметром масштаба"""
pen_up()
to_point(-5,f(-5))
pen_down()
#for x in range(-5,6,1):
    #to_point(x,f(x))

x=-5
while x<=5:
    to_point(x,f(x))
    x+=0.1
pen_up()
sleep(10)

