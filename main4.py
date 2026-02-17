import subprocess
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

def new_window_registration():
    def registration():
        new_login=entry_login_r.get()
        new_password = entry_password_r.get()
        with open("users.json", "r", encoding="utf-8") as f:
            users = json.load(f)
        with open("users.json", "w", encoding="utf-8") as f:
            users[hash_password(new_login)] = hash_password(new_password)
            json.dump(users, f, indent=4)
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
    username = hash_password(entry_login.get())
    password = hash_password(entry_password.get())
    print(username, password)
    if not username or not password:
        messagebox.showerror("Ошибка", "Введите логин и пароль!")

    with open("users.json", "r", encoding="utf-8") as f:
        users = json.load(f)

    if username in users and users[username] == password:
        messagebox.showinfo("Успешно", f"Добро пожаловать {entry_login.get()}")
        root.destroy()
        subprocess.run(['python',r"C:\Users\User\PycharmProjects\pythonProject3\calculator.py"])

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
entry_password = tk.Entry(root, width=25, show="*")
entry_password.pack(pady=5)

LogInButton=tk.Button(root, text = "Войти", command = login, width = 20, height = 5)
LogInButton.pack(pady=15)

RegButton = tk.Button(root, text = "Зарегистрироваться", command = new_window_registration, width = 20, height = 5)
RegButton.pack(pady=15)
root.mainloop()
