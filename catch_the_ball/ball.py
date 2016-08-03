import Tkinter

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


    label=Tkinter.Label(root,text='Some text')
    text=Tkinter.Entry(root)
    scale=Tkinter.Scale(root)
    for obj in label,text,scale:
        obj.pack()



if __name__=="__main__":
    init_main_window()

root.mainloop()