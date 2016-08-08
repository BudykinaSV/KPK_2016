from tkinter import *
from random import choice, randint

ball_initial_number=20
ball_maximal_radius=30
ball_minimal_radius=15
ball_available_colors=["lightgray","blue","red","#FFFF00","#FF00FF","#00FFFF"]


def init_game():
    """
    создание шариков и пушки
    """

def init_main_window():
    global root, canvas, scores_text, scores_value
    root=Tk()


if __name__=="__main__":
    init_main_window()
    init_game()
    root.mainloop()