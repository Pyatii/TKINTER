import tkinter as tk
from tkinter import messagebox
import json
import os
from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

if not  os.path.exists("users.json"):
    with open("users.json", "w", encoding="utf-8") as f:
        log = hash_password("admin")
        pas = hash_password("admin123")
        users = {
            log: pas
        }
        json.dump(users, f, indent=4)

def login():
    username = hash_password(entry_login.get())
    password = hash_password(entry_password.get())
    print(username, password)
    if not username or not password:
        messagebox.showerror("Ошибка", "Введите логин и пароль!")

    with open("users.json", "r", encoding="utf-8") as f:
        users = json.load(f)

    if username in users and users[username] == password:
        messagebox.showinfo("Успешно", f"Добро пожаловать {entry_login.get()}")
    else:
        messagebox.showinfo("Отказано в доступе", "Введите верный логин и пароль")
root = tk.Tk()
root.title("Авторизация")
root.geometry("300x400")
root.resizable(False, False)

Label1 = tk.Label(root, text = "Вход в систему")
Label1.pack(pady=15)

Label2=tk.Label(root, text="Логин: ")
Label2.pack()
entry_login = tk.Entry(root, width=25)
entry_login.pack(pady=5)

Label3 = tk.Label(root, text = "Пароль: ")
Label3.pack(pady=5)
entry_password = tk.Entry(root, width=25)
entry_password.pack(pady=5)

LogInButton=tk.Button(root, text = "Войти", command = login, width = 20, height = 5)
LogInButton.pack(pady=15)

root.mainloop()
