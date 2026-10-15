import tkinter as tk

clicks = 0
render: list = []


def isnum(num):
    if len(num) > 1:
        num = num[-1]
    return ord(num) > 47 and ord(num) < 58


def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def sub(num1, num2):
    return num1 / num2


tup = {'+': plus,
       '-': minus,
       '*': mul,
       'sub': sub
       }


def render_delite():
    current = display.get()
    if current:
        display.delete(len(current) - 1, tk.END)


def render_clear():
    render.clear()
    display.delete(0, tk.END)


def render_append(num):
    display.insert(tk.END, str(num))
    if len(render) != 0 and isnum(num) and isnum(render[-1]):
        num2 = render.pop(-1)
        num = num2 + num
    render.append(num)
    print(render)


def render_finalist():
    display.delete(0, tk.END)
    func = tup[render[1]]
    num1, num2 = int(render[0]), int(render[2])
    display.insert(tk.END, str(func(num1, num2)))
    render.clear()
    render.append(str(func(num1, num2)))


root = tk.Tk()
root.title("Calc")
root.geometry("500x500")

display = tk.Entry(root, font=("Arial", 20),
                   justify="right", bd=10, insertwidth=14, width=15)


btn1 = tk.Button(text="1", command=lambda: render_append('1'),
                 font=("Arial", 16))
btn2 = tk.Button(text="2", command=lambda: render_append('2'),
                 font=("Arial", 16))
btn3 = tk.Button(text="3", command=lambda: render_append('3'),
                 font=("Arial", 16))
btn4 = tk.Button(text="4", command=lambda: render_append('4'),
                 font=("Arial", 16))
btn5 = tk.Button(text="5", command=lambda: render_append('5'),
                 font=("Arial", 16))
btn6 = tk.Button(text="6", command=lambda: render_append('6'),
                 font=("Arial", 16))
btn7 = tk.Button(text="7", command=lambda: render_append('7'),
                 font=("Arial", 16))
btn8 = tk.Button(text="8", command=lambda: render_append('8'),
                 font=("Arial", 16))
btn9 = tk.Button(text="9", command=lambda: render_append('9'),
                 font=("Arial", 16))
btn0 = tk.Button(text="0", command=lambda: render_append('0'),
                 font=("Arial", 16))

btn_div = tk.Button(text="/", command=lambda: render_append("/"),
                    font=("Arial", 16))
btn_plus = tk.Button(text="+", command=lambda: render_append("+"),
                     font=("Arial", 16))
btn_minus = tk.Button(text="-", command=lambda: render_append("-"),
                      font=("Arial", 16))
btn_mul = tk.Button(text="*", command=lambda: render_append("*"),
                    font=("Arial", 16))

btn_backspace = tk.Button(text='⌫', command=lambda: render_delite(),
                          font=('Arial', 16))
btn_clear = tk.Button(text='🗑️', command=lambda: render_clear(),
                      font=('Arial', 16))
btn_equals = tk.Button(text='=', command=lambda: render_finalist(),
                       font=('Arial', 16))


btn1.grid(row=1, column=0, ipadx=30, ipady=15)
btn4.grid(row=2, column=0, ipadx=30, ipady=15)
btn7.grid(row=3, column=0, ipadx=30, ipady=15)

btn2.grid(row=1, column=1, ipadx=30, ipady=15)
btn5.grid(row=2, column=1, ipadx=30, ipady=15)
btn8.grid(row=3, column=1, ipadx=30, ipady=15)

btn3.grid(row=1, column=2, ipadx=30, ipady=15)
btn6.grid(row=2, column=2, ipadx=30, ipady=15)
btn9.grid(row=3, column=2, ipadx=30, ipady=15)

btn_plus.grid(row=1, column=3, ipadx=30, ipady=15)
btn_minus.grid(row=2, column=3, ipadx=30, ipady=15)
btn_mul.grid(row=3, column=3, ipadx=30, ipady=15)
btn_div.grid(row=4, column=3, ipadx=30, ipady=15)

btn_backspace.grid(row=5, column=0, ipadx=25, ipady=15)
btn_clear.grid(row=4, column=1, ipadx=25, ipady=15)
btn_equals.grid(row=4, column=2, ipadx=30, ipady=15)
btn0.grid(row=4,column=0,ipadx=30,ipady=15)

display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
