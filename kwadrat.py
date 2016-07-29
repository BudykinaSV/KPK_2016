from proba import *
from time import sleep

A=[(0,0),(100,0),(100,100),(0,100),(0,0)]
pen_down()
for x,y in A:
    to_point(x,y)
pen_down()
sleep(10)