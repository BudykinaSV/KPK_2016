from proba import *
from time import sleep
def f(x):
    return x**2
pen_up()
to_point(-5,f(-5))
pen_down()
for x in range(-5,6,1):
    to_point(x,f(x))
pen_up()
sleep(10)

