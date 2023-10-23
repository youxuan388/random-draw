import tkinter as tk
import random

def computerscissors():
    b=random.randint(1,3)
    if b==1:
        label = tk.Label(text="電腦出了剪刀")
        label.pack()
        label = tk.Label(text="平手")
        label.pack()
    elif b==2:
        label = tk.Label(text="電腦出了石頭")
        label.pack()
        label = tk.Label(text="你輸了")
        label.pack()
    elif b==3:
        label = tk.Label(text="電腦出了布")
        label.pack()
        label = tk.Label(text="你贏了")
        label.pack()
        
def computerstone():
    b=random.randint(1,3)
    if b==1:
        label = tk.Label(text="電腦出了剪刀")
        label.pack()
        label = tk.Label(text="你贏了")
        label.pack()
    elif b==2:
        label = tk.Label(text="電腦出了石頭")
        label.pack()
        label = tk.Label(text="平手")
        label.pack()
    elif b==3:
        label = tk.Label(text="電腦出了布")
        label.pack()
        label = tk.Label(text="你輸了")
        label.pack()
        
def computerpaper():
    b=random.randint(1,3)
    if b==1:
        label = tk.Label(text="電腦出了剪刀")
        label.pack()
        label = tk.Label(text="你輸了")
        label.pack()
    elif b==2:
        label = tk.Label(text="電腦出了石頭")
        label.pack()
        label = tk.Label(text="你贏了")
        label.pack()
    elif b==3:
        label = tk.Label(text="電腦出了布")
        label.pack()
        label = tk.Label(text="平手")
        label.pack()


def scissors():
    label = tk.Label(text="你出了剪刀")
    label.pack()
    computerscissors()
    
def stone():
    label = tk.Label(text="你出了石頭")
    label.pack()
    computerstone()
def paper():
    label = tk.Label(text="你出了布")
    label.pack()
    computerpaper()
window = tk.Tk()

window.geometry('500x500')
window.title('剪刀石頭布')

label = tk.Label(text="你要出什麼")
label.pack()

button = tk.Button(text = "剪刀",command=scissors)
button.pack()

button = tk.Button(text = "石頭",command=stone)
button.pack()

button = tk.Button(text = "布",command=paper)
button.pack()
window.mainloop()