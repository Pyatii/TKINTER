import tkinter as tk
import random
from tkinter import messagebox
import math

def calculate():
    var = opt.get()
    if var == values[0]:
        plus()
    elif var == values[1]:
        minus()
    elif var == values[2]:
        multi()
    elif var == values[3]:
        div()
    elif var == values[4]:
        factorial()
    elif var == values[5]:
        sinus()
    elif var == values[6]:
        cosinus()

def plus():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        result = num1 + num2
        label_res.config(text = f'Результат {result}')
    except:
        messagebox.showerror('Ошибка', 'Введите числа')

def minus():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        label_res.config(text=f'Результат {result}')
    except:
        messagebox.showerror('Ошибка', 'Введите числа')

def multi():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        label_res.config(text=f'Результат {result}')
    except:
        messagebox.showerror('Ошибка', 'Введите числа')

def div():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1/num2
        label_res.config(text=f'Результат {result}')
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'Деление на ноль')
    except:
        messagebox.showerror('Ошибка', 'Введите числа')

def factorial():
    try:
        num1 = int(entry1.get())
        result = math.factorial(num1)
        label_res.config(text=f'Результат {result}')
    except:
        messagebox.showerror('Ошибка', 'Введите ЦЕЛОЕ число')

def sinus():
    try:
        num1=float(entry1.get())
        if trigon == 0:
            num1 = math.degrees(num1)
        result = math.sin(num1)
        label_res['text'] = f'Результат {result}'
    except:
        messagebox.showerror('Ошибка', 'Введите число')
def cosinus():
    try:
        num1=float(entry1.get())
        result = math.cos(num1)
        label_res['text'] = result
    except:
        messagebox.showerror('Ошибка', 'Введите число')

def mouse_left_on_click(event):
    color ='#'+ '{:06x}'.format(random.randint(0,16777216))
    root['bg'] = color


def mouse_right_on_click(event):
    pass

def change_frames(*args):
    global trigon
    flag=opt.get()
    entry_frame1.pack_forget()
    entry_frame2.pack_forget()
    if flag in values[0:4]:
        entry_frame1.pack(pady=5)
        entry_frame2.pack(pady=5)
    if flag in values[4:]:
        entry_frame1.pack(pady=5)
        if flag in values[5:7]:
            trigon=messagebox.askyesno('Выберите', 'Да=Радианы, Нет=Градусы')



root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

entrys_frame = tk.Frame(root)
entrys_frame.pack(pady=5)

entry_frame1 = tk.Frame(entrys_frame)

label1 = tk.Label(entry_frame1, text = "Значение 1:")
label1.pack(side = tk.LEFT, pady = 5)

entry1 = tk.Entry(entry_frame1)
entry1.pack(side = tk.LEFT, pady = 5)

entry_frame2 = tk.Frame(entrys_frame)


label2 = tk.Label(entry_frame2, text = "Значение 2:")
label2.pack(side = tk.LEFT, pady = 5)

entry2 = tk.Entry(entry_frame2)
entry2.pack(side = tk.LEFT, pady = 5)

res_frame = tk.Frame(root)
res_frame.pack(pady=5)

calc_button = tk.Button(res_frame, text = "Посчитать", command = calculate)
calc_button.pack(side = tk.LEFT, pady=5)

values=["Сложить", "Вычесть", "Умножить", "Делить", "Факториал", "Синус", "Косинус"]
opt = tk.StringVar(value="Сложить")
opt.trace('w', change_frames)

combo = tk.OptionMenu(res_frame, opt, *values)
combo.pack(side = tk.LEFT, pady=5)

label_res = tk.Label(root, text="Результат: ")
label_res.pack(pady=5)

root.bind('<Button-1>', mouse_left_on_click)
root.bind('<Button-2>', mouse_right_on_click)

root.mainloop()
