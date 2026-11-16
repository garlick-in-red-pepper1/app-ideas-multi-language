import math as mt

import customtkinter as ctk  # type: ignore

typer: str = 'dollars'


def JN(num: str):
    """check that symbol if number or '.|,'"""
    return num in "1234567890.,"


def num_checker(num: str) -> bool:
    """check that string is numbers and '.|,'"""
    checker: str = ''.join(list(filter(JN, num)))
    return checker == num


def change_type(entry) -> None:
    """changing type of input numbers (cents|dollars)"""
    global typer
    if typer == 'dollars':
        entry.configure(placeholder_text="insert sum in cents")
        typer = 'cents'
    else:
        entry.configure(placeholder_text="insert sum in dollars")
        typer = 'dollars'


def make_num(num: str) -> int:
    if typer == 'dollars':
        return mt.ceil(float(num) * 100)
    else:
        return int(num)


def exchange_quarters(num: int) -> dict[str, int | bool]:
    base: dict[str, int | bool] = {}
    base['quarter'] = num // 25
    base['remainder'] = num % 25
    base['status'] = True
    return base


def exchange_dimes(num: int) -> dict[str, int | bool]:
    base: dict[str, int | bool] = exchange_quarters(num)
    num = base['remainder']
    base['dimes'] = num // 10
    base['remainder'] = num % 10
    return base


def exchange_nickel(num: int) -> dict[str, int | bool]:
    base: dict[str, int | bool] = exchange_dimes(num)
    num = base['remainder']
    base['nickel'] = num // 5
    base['pennies'] = num % 5
    return base


def exchanger(dollar_sum: str) -> dict[str, int | bool]:

    if exchanger(dollar_sum) is False:
        return {"status": False}

    else:
        summ: int = make_num(dollar_sum)
        return exchange_nickel(summ)


def process_input(entry, label_cents, label_quarters, label_dimes,
                  label_nickels, label_pennies):

    user_text: any = entry.get()  # type: ignore

    if num_checker(user_text):
        num: int = make_num(user_text)  # type: ignore
        nums: dict[str, int | bool] = exchange_nickel(num)  # type: ignore
        label_cents.configure(text=f'total cents: {num}')
        label_quarters.configure(text=f'total quarters: {nums['quarter']}')
        label_dimes.configure(text=f'total dimes: {nums['dimes']}')
        label_nickels.configure(text=f'total nickels: {nums['nickel']}')
        label_pennies.configure(text=f'total pennies: {nums['pennies']}')


def nothing() -> int:
    return 0


def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title("exchanger")
    app.geometry("500x400")

    entry = ctk.CTkEntry(
                         app,
                         placeholder_text="insert sum in dollars",
                         width=250,
                         height=40,
                         corner_radius=8
    )
    entry.grid(row=0, column=0, padx=15, pady=30)
    label_cent = ctk.CTkLabel(app, text="total cents",
                              font=("Helvetica", 14))
    label_quarter = ctk.CTkLabel(app, text="total quarters",
                                 font=("Helvetica", 14))
    label_dimes = ctk.CTkLabel(app, text="total dimes",
                               font=("Helvetica", 14))
    label_nickel = ctk.CTkLabel(app, text="total nickels",
                                font=("Helvetica", 14))
    label_pennie = ctk.CTkLabel(app, text="total pennies",
                                font=("Helvetica", 14))

    button_type = ctk.CTkButton(app, text='change: cents/dollars',
                                command=lambda: change_type(entry))
    button_convert = ctk.CTkButton(app, text="convert",
                                   command=lambda: process_input(entry,
                                                                 label_cent,
                                                                 label_quarter,
                                                                 label_dimes,
                                                                 label_nickel,
                                                                 label_pennie))
    button_convert.grid(row=1, column=0, padx=15, pady=30)

    label_cent.grid(row=2, column=0, padx=15, pady=30)
    label_quarter.grid(row=3, column=0, padx=15, pady=30)
    label_dimes.grid(row=1, column=1, padx=15, pady=30)
    label_nickel.grid(row=2, column=1, padx=15, pady=30)
    label_pennie.grid(row=3, column=1, padx=15, pady=30)
    button_type.grid(row=0, column=1, padx=15, pady=30)

    app.mainloop()
