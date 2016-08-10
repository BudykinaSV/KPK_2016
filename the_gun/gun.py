from tkinter import *
from random import choice, randint

screen_width=400
screen_height=300
timer_delay=100

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


    def fly(self):
        self._x+=self._Vx
        self._y+=self._Vy
        #отражение от стенок
        if self._x<0:
            self._x=0
            self._Vx=-self._Vx
        elif self._x+2*self._R>=screen_width:
            self._x=screen_width-2*self._R-1
            self._Vx=-self._Vx
        if self._y<0:
            self._y=0
            self._Vy=-self._Vy
        elif self._y+2*self._R>=screen_height:
            self._y=screen_height-2*self._R-1
            self._Vy=-self._Vy

        canvas.coords(self._avatar,self._x,self._y,
                      self._x+2*self._R,self._y+2*self._R)



class Gun:
    """КЛАСС пука"""
    def __init__(self):
        self._x = 2
        self._y = screen_height-1
        self._lx = +30
        self._ly = -30
        self._avatar = canvas.create_line(self._x, self._y,
                        self._x+self._lx, self._y+self._ly)

        self._avatar = canvas.create_line(self._x+10, self._y,
                        self._x+self._lx+10, self._y+self._ly)

        self._avatar = canvas.create_line(self._x, self._y,
                        self._x+10, self._y)
        self._avatar = canvas.create_line(self._x+self._lx, self._y+self._ly,
                        self._x+self._lx+10, self._y+self._ly)

    def shoot(self):
        """
        метод СНАРЯД, возвращает объект снаряда (класса Ball)
        """
        shell= Ball()
        shell._x=self._x+self._lx-3
        shell._y=self._y+self._ly-6
        shell._Vx=self._lx/10
        shell._Vy=self._ly/10
        shell._R=5
        shell.fly()
        return shell


def init_game():
    """
    создание шариков и пушки
    """
    global balls, gun, shells_on_fly
    balls=[Ball() for i in range(Ball.initial_number)]
    gun = Gun() #создать экземпляр пушки
    shells_on_fly = []


def init_main_window():
    global root, canvas, scores_text, scores_value
    root = Tk()
    root.title('Пушка')
    scores_value=IntVar()
    canvas = Canvas(root, width=screen_width, height=screen_height, bg="#ffffff")
    scores_text = Entry(root, textvariable=scores_value)
    canvas.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0,column=2)
    canvas.bind('<Button-1>', click_event_handler)

def timer_event():
    #print('Tik-tak')
    for ball in balls:
        ball.fly()
    for shell in shells_on_fly:
        shell.fly()


    canvas.after(timer_delay, timer_event)#каждые 2сек пишем hello

def click_event_handler(event):
    global shells_on_fly
    shell = gun.shoot()
    shells_on_fly.append(shell)

if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()