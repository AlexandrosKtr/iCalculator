import tkinter as tk
from tkinter import messagebox


def main():
    calculator = Calculator()
    calculator.root.mainloop()


class Calculator():
    def __init__(self):
        self.root = create_root()
        self.entry = create_entry(self.root)
        self.operator = ""
        self.temp = ""
        self.new = True
        create_buttons(self)


def create_root():
    """Create the main application window"""

    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x600")
    root.resizable(False, False)
    root.configure(bg="black")
    return root

def create_entry(root):
    """Create an entry widget for the input"""

    entry = tk.Entry(
        root,
        width=17,
        borderwidth=0,
        font=("Arial", 30),
        justify="right",
        bg="black",
        fg="white",
    )
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
    entry.insert(0, "0")
    return entry


def create_buttons(calculator):
    """Create the buttons display"""

    # Button styles
    button_font = ("Arial", 18)
    button_bg = "#333333"
    button_fg = "white"
    button_active_bg = "#666666"

    top_button_bg = "gray"
    top_button_fg = "black"
    top_button_active_bg = "#666666"
    top_button_active_fg = top_button_fg

    operator_bg = "#ff9500"
    operator_fg = "white"
    operator_active_bg = "white"
    operator_active_fg = "#ff9500"

    # Define button texts and their grid positions
    buttons = [
        ("+/-", 1, 1, button_negative, top_button_bg),
        ("%", 1, 2, button_percentage, top_button_bg),
        ("7", 2, 0, button_num, button_bg),
        ("8", 2, 1, button_num, button_bg),
        ("9", 2, 2, button_num, button_bg),
        ("4", 3, 0, button_num, button_bg),
        ("5", 3, 1, button_num, button_bg),
        ("6", 3, 2, button_num, button_bg),
        ("1", 4, 0, button_num, button_bg),
        ("2", 4, 1, button_num, button_bg),
        ("3", 4, 2, button_num, button_bg),
        ("0", 5, 0, button_num, button_bg, 2),
        (".", 5, 2, button_comma, button_bg),
        ("=", 5, 3, button_equal, operator_bg),
    ]

    # Create buttons and add them to the grid
    for button in buttons:
        if len(button) == 5:
            text, row, col, command, bg = button
            colspan = 1
        else:
            text, row, col, command, bg, colspan = button

        btn = tk.Button(
            calculator.root,
            text=text,
            width=5,
            height=2,
            font=button_font,
            bg=bg,
            fg=top_button_fg if text in ["C", "+/-", "%"] else button_fg,
            activebackground=button_active_bg,
            activeforeground=(
                top_button_fg if text in ["C", "+/-", "%"] else button_fg
            ),
            command=lambda text=text, command=command: (
                command(calculator, text) if text.isdigit() else command(calculator)
            ),
        )
        btn.grid(
            row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew"
        )

    calculator.btn_clear = tk.Button(
        calculator.root,
        text="AC",
        width=5,
        height=2,
        font=button_font,
        bg=top_button_bg,
        fg=top_button_fg,
        activebackground=top_button_active_bg,
        activeforeground=top_button_active_fg,
        command=lambda: (
            button_clear_all(calculator)
            if calculator.btn_clear["text"] == "AC"
            else button_clear(calculator)
        ),
    )
    calculator.btn_clear.grid(
        row=1, column=0, columnspan=1, padx=5, pady=5, sticky="nsew"
    )
    calculator.btn_plus = tk.Button(
        calculator.root,
        text="+",
        width=5,
        height=2,
        font=button_font,
        bg=operator_bg,
        fg=operator_fg,
        activebackground=operator_active_bg,
        activeforeground=operator_active_fg,
        command=lambda: button_operator(calculator, "+"),
    )
    calculator.btn_plus.grid(row=4, column=3, columnspan=1, padx=5, pady=5, sticky="nsew")
    calculator.btn_minus = tk.Button(
        calculator.root,
        text="-",
        width=5,
        height=2,
        font=button_font,
        bg=operator_bg,
        fg=operator_fg,
        activebackground=operator_active_bg,
        activeforeground=operator_active_fg,
        command=lambda: button_operator(calculator, "-"),
    )
    calculator.btn_minus.grid(
        row=3, column=3, columnspan=1, padx=5, pady=5, sticky="nsew"
    )
    calculator.btn_multiply = tk.Button(
        calculator.root,
        text="*",
        width=5,
        height=2,
        font=button_font,
        bg=operator_bg,
        fg=operator_fg,
        activebackground=operator_active_bg,
        activeforeground=operator_active_fg,
        command=lambda: button_operator(calculator, "*"),
    )
    calculator.btn_multiply.grid(
        row=2, column=3, columnspan=1, padx=5, pady=5, sticky="nsew"
    )
    calculator.btn_subtract = tk.Button(
        calculator.root,
        text="/",
        width=5,
        height=2,
        font=button_font,
        bg=operator_bg,
        fg=operator_fg,
        activebackground=operator_active_bg,
        activeforeground=operator_active_fg,
        command=lambda: button_operator(calculator, "/"),
    )
    calculator.btn_subtract.grid(
        row=1, column=3, columnspan=1, padx=5, pady=5, sticky="nsew"
    )

    # Make the buttons expand when the window is resized
    for i in range(6):
        calculator.root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        calculator.root.grid_columnconfigure(i, weight=1)


def button_num(calculator, num):
    """Adds the specified number to the operation"""

    if calculator.entry.get() == "0" and num == "0":
        return
    
    elif not calculator.operator:

        if calculator.new:
            calculator.new = False

            calculator.entry.delete(0, tk.END)
            calculator.entry.insert(tk.END, str(num))
        else:
            calculator.entry.insert(tk.END, str(num))

    else:

        if calculator.new:
            calculator.temp = calculator.entry.get()
            calculator.new = False

            calculator.entry.delete(0, tk.END)
            calculator.entry.insert(tk.END, str(num))
        else:
            calculator.entry.insert(tk.END, str(num))

    calculator.btn_clear.configure(text="C")


def button_comma(calculator):
    """Adds a comma"""

    curr = calculator.entry.get()

    if "." not in curr:
        calculator.entry.insert(tk.END, ".")
        calculator.new = False


def button_clear(calculator):
    """Clears the displayed number"""

    calculator.new = True

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "0")
    calculator.btn_clear.configure(text="AC")

def button_clear_all(calculator):
    """Resets the calculator"""

    calculator.operator = ""
    calculator.temp = ""
    calculator.new = True

    toggle(calculator)

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "0")

def button_equal(calculator):
    """Displays the result of the current operation"""

    toggle(calculator)

    if calculator.operator:
        curr = calculator.temp + calculator.operator + calculator.entry.get()
        calculator.temp = calculator.operator + calculator.entry.get()
    else:
        curr = calculator.entry.get() + calculator.temp

    try:
        result = str(eval(curr))
        if float(result) % 1 == 0:
            result = str(int(float(result)))

        calculator.entry.delete(0, tk.END)
        calculator.entry.insert(tk.END, result)

    except ZeroDivisionError as ex:
        calculator.entry.delete(0, tk.END)
        calculator.entry.insert(tk.END, "Error")
        messagebox.showerror("ZeroDivisionError", "Cannot divide by 0")

    except Exception as ex:
        calculator.entry.delete(0, tk.END)
        calculator.entry.insert(tk.END, "Error")
        messagebox.showerror("Error", "Invalid Input")

    calculator.operator = ""
    calculator.new = True

def button_operator(calculator, op):
    """Adds the operator"""

    toggle(calculator, op)

    if calculator.operator and calculator.operator != op:
        curr = calculator.temp + calculator.operator + calculator.entry.get()
        calculator.temp = calculator.operator + calculator.entry.get()

        try:
            result = str(eval(curr))
            if float(result) % 1 == 0:
                result = str(int(float(result)))

            calculator.entry.delete(0, tk.END)
            calculator.entry.insert(tk.END, result)

        except ZeroDivisionError as ex:
            calculator.entry.delete(0, tk.END)
            calculator.entry.insert(tk.END, "Error")
            messagebox.showerror("ZeroDivisionError", "Cannot divide by 0")

        except Exception as ex:
            calculator.entry.delete(0, tk.END)
            calculator.entry.insert(tk.END, "Error")
            messagebox.showerror("Error", "Invalid Input")

    calculator.operator = op
    calculator.new = True

def button_percentage(calculator):
    """Displays the current number in a percentage type"""

    try:
        curr = str(float(calculator.entry.get()) / 100)
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")
    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, curr)

def button_negative(calculator):
    """Toggles between negative and positive numbers"""

    curr = calculator.entry.get()
    if curr:
        if curr[0] == "-":
            calculator.entry.delete(0, 1)
        else:
            calculator.entry.insert(0, "-")

def toggle(calculator, operator=""):
    match operator:
        case "+":
            calculator.btn_plus.configure(bg="white", fg="#ff9500")
            calculator.btn_minus.configure(bg="#ff9500", fg="white")
            calculator.btn_multiply.configure(bg="#ff9500", fg="white")
            calculator.btn_subtract.configure(bg="#ff9500", fg="white")
        case "-":
            calculator.btn_plus.configure(bg="#ff9500", fg="white")
            calculator.btn_minus.configure(bg="white", fg="#ff9500")
            calculator.btn_multiply.configure(bg="#ff9500", fg="white")
            calculator.btn_subtract.configure(bg="#ff9500", fg="white")
        case "*":
            calculator.btn_plus.configure(bg="#ff9500", fg="white")
            calculator.btn_minus.configure(bg="#ff9500", fg="white")
            calculator.btn_multiply.configure(bg="white", fg="#ff9500")
            calculator.btn_subtract.configure(bg="#ff9500", fg="white")
        case "/":
            calculator.btn_plus.configure(bg="#ff9500", fg="white")
            calculator.btn_minus.configure(bg="#ff9500", fg="white")
            calculator.btn_multiply.configure(bg="#ff9500", fg="white")
            calculator.btn_subtract.configure(bg="white", fg="#ff9500")
        case _:
            calculator.btn_plus.configure(bg="#ff9500", fg="white")
            calculator.btn_minus.configure(bg="#ff9500", fg="white")
            calculator.btn_multiply.configure(bg="#ff9500", fg="white")
            calculator.btn_subtract.configure(bg="#ff9500", fg="white")


if __name__ == "__main__":
    main()
