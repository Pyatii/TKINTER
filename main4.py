import subprocess
import tkinter as tk
from tkinter import messagebox
import json
import os
from hashlib import sha256
from test import Database
def hash_password(password):
    return sha256(password.encode()).hexdigest()

def new_window_registration():
    def registration():
        username = entry_login_r.get()
        password = hash_password(entry_password_r.get())


        if db.write(f"""
        INSERT INTO users(login, password)
        VALUES (?, ?)""", [username, password]):
            messagebox.showinfo("Успешно", f"Вы зарегистрированы")
        else:
            messagebox.showerror("Неуспешно", f"Вы не зарегистрированы")



    root_w= tk.Toplevel(root)
    root_w.title("Регистрация нового пользователя")
    root_w.geometry("300x400")
    root_w.resizable(False, False)

    root_w.grab_set()
    root_w.focus_set()

    title_label=tk.Label(root_w, text="Регистрация")
    title_label.pack(pady=10)

    entry_label = tk.Label(root_w, text="Новый логин")
    entry_label.pack(pady=10)
    entry_login_r = tk.Entry(root_w, width=30)
    entry_login_r.pack(pady=10)

    entry1_label = tk.Label(root_w, text="Новый пароль")
    entry1_label.pack(pady=10)
    entry_password_r = tk.Entry(root_w, width=30)
    entry_password_r.pack(pady=10)

    reg_button = tk.Button(root_w, text="Регистрация", command = registration, width=15)
    reg_button.pack(pady=15)

def login():
    username = entry_login.get()
    password = hash_password(entry_password.get())
    print(username, password)
    if not username or not password:
        messagebox.showerror("Ошибка", "Введите логин и пароль!")
    if password == db.read(f"""
    SELECT password
    FROM users
    WHERE login = ?
    """, [username])[0][0]:
        messagebox.showinfo("Успешно", f"Добро пожаловать {entry_login.get()}")

    else:
        messagebox.showinfo("Отказано в доступе", "Введите верный логин и пароль")

def change():
    username = entry_login.get()
    password = hash_password(entry_password.get())
    if not username or not password:
        messagebox.showerror("Ошибка", "Введите логин и пароль!")
    print(f"""
        UPDATE users
        SET password = ?
        WHERE login = ? """)
    if db.write(f"""
    UPDATE users
    SET password = ?
    WHERE login = ? """, [password, username]):
        messagebox.showinfo("Успешно", f"Пароль изменен")

    else:
        messagebox.showinfo("Отказано в доступе", "Неизвестная ошибка")



db = Database()
root = tk.Tk()
root.title("Авторизация")
root.geometry("300x600")
root.resizable(False, False)

Label1 = tk.Label(root, text = "Вход в систему")
Label1.pack(pady=15)

Label2=tk.Label(root, text="Логин: ")
Label2.pack()
entry_login = tk.Entry(root, width=25)
entry_login.pack(pady=5)

Label3 = tk.Label(root, text = "Пароль: ")
Label3.pack(pady=5)
entry_password = tk.Entry(root, width=25, show="*")
entry_password.pack(pady=5)

LogInButton=tk.Button(root, text = "Войти", command = login, width = 20, height = 5)
LogInButton.pack(pady=15)

RegButton = tk.Button(root, text = "Зарегистрироваться", command = new_window_registration, width = 20, height = 5)
RegButton.pack(pady=15)

ChangeButton = tk.Button(root, text = "Изменить", command = change, width = 20, height = 5)
ChangeButton.pack(pady=15)

root.mainloop()
