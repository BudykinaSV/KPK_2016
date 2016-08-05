from proba import *
from time import sleep

A=[(0,0),(10,0),(10,10),(0,10),(0,0)]
pen_down()
for x,y in A:
    to_point(x,y)
pen_up()
sleep(10)
#