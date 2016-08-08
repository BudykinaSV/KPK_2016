from tkinter import *
from random import choice, randint

screen_width=400
screen_height=400
timer_delay=2000

class Ball:
    initial_number=10
    maximal_radius=30
    minimal_radius=15
    available_colors=["blue","red","green"]

    def __init__(self):
        """шарик в случайном положении"""
        R=randint(Ball.minimal_radius,Ball.maximal_radius)
        x=randint(0+R,screen_width-1-2*R)
        y=randint(0+R,screen_height-1-2*R)
        self._R=R
        self._x=x
        self._y=y
        R_color=choice(Ball.available_colors)
        self._avatar=canvas.create_oval(x,y,x+2*R,y+2*R,fill=R_color,width=1, outline="#000000")

        self._Vx=randint(-2,2)
        self._Vy=randint(-2,2)



def init_game():
    """
    создание шариков и пушки
    """
    global balls
    balls=[Ball() for i in range(Ball.initial_number)]


def init_main_window():
    global root, canvas, scores_text, scores_value
    root = Tk()
    root.title('Пушка')
    scores_value=IntVar()
    canvas = Canvas(root, width=screen_width, height=screen_height, bg="#ffffff")
    scores_text = Entry(root, textvariable=scores_value)
    canvas.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0,column=2)

def timer_event():
    print('Hello')
    canvas.after(timer_delay, timer_event)#каждые 2сек пишем hello

if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()