import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)

    if value == "C":
        entry.insert(0, "")
    elif value == "=":
        try:
            result = eval(current)
            entry.insert(0, str(result))
        except:
            entry.inser(0, "Ошибка")
    elif value == "X":
        entry.insert(0, current[:-1])
    else:
        entry.insert(0, current+value)

# Основное окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x450")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Поле ввода
entry = tk.Entry(root, justify = "right", bd = 10, relief = tk.RIDGE)
entry.grid(row = 0, column = 0, columnspan = 4, padx=10, pady = 10, ipady = 10, sticky="ew")

#Кнопки ввода

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "X", "(", ")"]
]

button_styles = {
    "number": {"bg": "#e0e0e0", "activebackground": "#d0d0d0"},
    "operator": {"bg": "#ff0000", "activebackground": "#00ff00"},
    "clear": {"bg": "#0000ff", "activebackground": "#f0f0f0"},
    "equals": {"bg": "#4caf50", "activebackground": "#f5f5f5"}
}

for row_idx, row in enumerate(buttons):
    for col_idx, value in enumerate(row):
        if value in "0123456789.":
            style = button_styles["number"]
        elif value in "+-*/()":
            style = button_styles["operator"]
        elif value in "CX":
            style = button_styles["equals"]
        btn = tk.Button(
            root,
            text = value,
            command = lambda v=value: click_button(v),
            **style,
            relief = tk.RAISED,
            bd = 3

        )

        btn.grid(row=row_idx + 1, column=col_idx, padx=2, pady=2, sticky="nsew")

for i in range(1, len(buttons)+1):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
