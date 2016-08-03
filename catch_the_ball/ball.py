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

root=Tkinter.Tk()

button1=Tkinter.Button(root,text='Button1',command=button1_command)
button1.bind('<Button>',print_hello)
button1.pack()
button2=Tkinter.Button(root,text='Button2')
button2.bind('<Button>',print_hello)
button2.pack()

root.mainloop()