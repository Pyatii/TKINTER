import tkinter as tk
import random
from tkinter import messagebox
import math



root = tk.Tk()
root.title("Выберите оценку")
root.geometry("300x400")

def jump(*args):
    x=random.randint(0,300)
    y=random.randint(0,400)
    btn1.place(x=x, y=y)
def info():
    messagebox.showinfo('Оценка', 'Не повезло')
label1=tk.Label(text='Какую оценку вы хотите получить?')
label1.place(x=20, y=0)
btn1=tk.Button(text='Пять', bg = 'green')
btn1.place(x=20, y=20)
btn2=tk.Button(text='Два', command = info, bg='red')
btn2.place(x=100, y=20)
btn1.bind('<Motion>', jump)
root.mainloop()
