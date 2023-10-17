import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Cool Calculator")
        master.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 14), padding=10)

        self.entry_display = ttk.Entry(self.master, width=20, font=('Arial', 14), justify='right')
        self.entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        button_layout = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in button_layout:
            button = ttk.Button(self.master, text=text, command=lambda t=text: self.click_button(t), width=5, style='TButton.Primary.TButton' if text not in ('C', '=') else f'TButton.{text}.TButton')
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def click_button(self, symbol):
        if symbol == '=':
            self.calculate()
        elif symbol == 'C':
            self.clear_display()
        else:
            current_text = self.entry_display.get()
            self.entry_display.delete(0, tk.END)
            self.entry_display.insert(tk.END, current_text + symbol)

    def clear_display(self):
        self.entry_display.delete(0, tk.END)

    def calculate(self):
        try:
            expression = self.entry_display.get()
            result = eval(expression)
            self.entry_display.delete(0, tk.END)
            self.entry_display.insert(tk.END, str(result))
        except Exception as e:
            self.entry_display.delete(0, tk.END)
            self.entry_display.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
