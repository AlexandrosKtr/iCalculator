from iCalculator_2_testable import *


def main():
    test_button_num()
    test_button_comma()
    test_button_clear()
    test_button_clear_all()
    test_button_equal()
    test_button_operator()
    test_button_percentage()
    test_button_negative()


def test_button_num():
    calculator = Calculator()

    button_num(calculator, "0")
    assert(calculator.entry.get()) == "0"

    button_num(calculator, "3")
    assert(calculator.entry.get()) == "3"

    button_num(calculator, "5")
    assert(calculator.entry.get()) == "35"


def test_button_comma():
    calculator = Calculator()

    button_comma(calculator)
    assert(calculator.entry.get()) == "0."

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "3.5")
    button_comma(calculator)
    assert(calculator.entry.get()) == "3.5"

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "-5")
    button_comma(calculator)
    assert(calculator.entry.get()) == "-5."


def test_button_clear():
    calculator = Calculator()

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "100")
    button_clear(calculator)
    assert(calculator.entry.get()) == "0"
    assert(calculator.btn_clear["text"]) == "AC"

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "-5")
    button_clear(calculator)
    assert(calculator.entry.get()) == "0"
    assert(calculator.btn_clear["text"]) == "AC"

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "0.54")
    button_clear(calculator)
    assert(calculator.entry.get()) == "0"
    assert(calculator.btn_clear["text"]) == "AC"
    

def test_button_clear_all():
    calculator = Calculator()

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "36")
    calculator.operator = "+"
    calculator.temp = "12"
    calculator.new = False

    button_clear_all(calculator)
    assert(calculator.entry.get()) == "0"
    assert(calculator.operator) == ""
    assert(calculator.temp) == ""
    assert(calculator.new) == True
    


def test_button_equal():
    calculator = Calculator()

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "5")
    calculator.operator = "+"
    calculator.temp = "8"
    button_equal(calculator)
    assert(calculator.entry.get()) == "13"
    assert(calculator.operator) == ""
    assert(calculator.temp) == "+5"

    button_clear_all(calculator)
    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "5")
    calculator.operator = "+"
    button_equal(calculator)
    assert(calculator.entry.get()) == "5"
    button_equal(calculator)
    assert(calculator.entry.get()) == "10"


def test_button_operator():
    calculator = Calculator()

    button_operator(calculator, "+")
    assert(calculator.operator) == "+"

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "3")
    calculator.temp = "2"
    button_operator(calculator, "-")
    assert(calculator.entry.get()) == "5"
    assert(calculator.operator) == "-"


def test_button_percentage():
    calculator = Calculator()

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "5")
    button_percentage(calculator)
    assert(calculator.entry.get()) == "0.05"

    button_percentage(calculator)
    assert(calculator.entry.get()) == "0.0005"


def test_button_negative():
    calculator = Calculator()

    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(tk.END, "5")
    button_negative(calculator)
    assert(calculator.entry.get()) == "-5"

    button_negative(calculator)
    assert(calculator.entry.get()) == "5"


if __name__ == "__main__":
    main()