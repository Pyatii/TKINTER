import tkinter as tk
import random
from tkinter import messagebox
import math


def mouse_left_on_click(event):
    color ='#'+ '{:06x}'.format(random.randint(0,16777216))
    root['bg'] = color
def plusminus(number):
    if number>0:
        return "+"
    elif number<0:
        return "-"
    return ""
def calculate():
    try:
        A=int(entryA.get())
        B = int(entryB.get())
        C = int(entryC.get())
        labelUrav['text'] = f"{A}x^2{plusminus(B)}{abs(B)}x{plusminus(C)}{abs(C)}=0"
        D=B**2 - 4*A*C
        x1=(-B+math.sqrt(D))/(2*A)
        x2=(-B-math.sqrt(D))/(2*A)

        X1label['text']=f"X1={x1}"
        X2label['text']=f"X2={x2}"
    except:
        X1label['text'] = "Уравнение имеет отрицательный дискриминант"
        X2label['text'] = f""

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

entrys_frame = tk.Frame(root)
labelA = tk.Label(entrys_frame, text = "A: ")
labelA.pack(side=tk.LEFT)
entryA = tk.Entry(entrys_frame, width=10)
entryA.pack(side=tk.LEFT, pady=5)
labelB = tk.Label(entrys_frame, text = "B: ")
labelB.pack(side=tk.LEFT, pady = 5)
entryB = tk.Entry(entrys_frame, width=10)
entryB.pack(side=tk.LEFT, pady=5)
labelC = tk.Label(entrys_frame, text = "C: ")
labelC.pack(side=tk.LEFT, pady = 5)
entryC = tk.Entry(entrys_frame, width=10)
entryC.pack(side=tk.LEFT, pady=5)
entrys_frame.pack(pady=5)

output_frame = tk.Frame(root)
labelUrav = tk.Label(output_frame, text = "Ax^2 + Bx + C")
labelUrav.pack(pady=5)
output_frame.pack(pady=5)
x_frame = tk.Frame(root)
X1label=tk.Label(x_frame, text="X1")
X2label=tk.Label(x_frame, text="X2")
X1label.pack(side=tk.LEFT)
X2label.pack(side=tk.LEFT)
x_frame.pack(pady=5)
button=tk.Button(root,text="ПОСЧИТАТЬ", command = calculate)
button.pack()
root.bind('<Button-1>', mouse_left_on_click)

root.mainloop()
