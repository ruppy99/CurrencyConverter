from tkinter import *
import tkinter as tk
from tkinter import ttk
import re


def restrict_number_only(action, string):
    regex = re.compile(r"[0-9]*?(\.)?[0-9]*$")
    result = regex.match(string)
    return string == "" or (string.count('.') <= 1 and result is not None)


class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        # self.configure(background = 'blue')
        self.geometry("500x200")

        # Label
        self.intro_label = Label(self, text='Currency Converter', fg='blue', relief=tk.RAISED,
                                 borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))

        self.date_label = Label(self,
                                text=f"Date : {self.currency_converter.data['date']}",
                                relief=tk.GROOVE, borderwidth=5)

        self.intro_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.date_label.place(relx=0.5, rely=0.4, anchor=CENTER)

        # Entry box
        valid = (self.register(restrict_number_only), '%d', '%P')
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE,
                                                  justify=tk.CENTER, width=17, borderwidth=3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("EUR")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")  # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.currency_converter.currencies.keys()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.currencies.keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)

        # placing
        self.from_currency_dropdown.place(relx=0.2, rely=0.6, anchor=CENTER)
        self.amount_field.place(relx=0.2, rely=0.8, anchor=CENTER)
        self.to_currency_dropdown.place(relx=0.8, rely=0.6, anchor=CENTER)
        self.converted_amount_field_label.place(relx=0.8, rely=0.8, anchor=CENTER)

        # Convert button
        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text=str(converted_amount))
