import tkinter as tk
from tkinter import ttk

import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Cool Password Generator")

        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12), padding=10)
        style.configure('TButton', font=('Arial', 12))
        style.configure('TCheckbutton', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12), padding=10)

        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self.master, text="Password Generator", style='TLabel')
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


        length_label = ttk.Label(self.master, text="Password Length:", style='TLabel')
        length_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')

        self.length_entry = ttk.Entry(self.master, textvariable=tk.StringVar(value="12"), width=5, style='TEntry')
        self.length_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')


        self.uppercase_check_var = tk.BooleanVar(value=True)
        self.lowercase_check_var = tk.BooleanVar(value=True)
        self.numbers_check_var = tk.BooleanVar(value=True)
        self.special_chars_check_var = tk.BooleanVar(value=True)

        uppercase_check = ttk.Checkbutton(self.master, text="Uppercase", variable=self.uppercase_check_var, style='TCheckbutton')
        uppercase_check.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        lowercase_check = ttk.Checkbutton(self.master, text="Lowercase", variable=self.lowercase_check_var, style='TCheckbutton')
        lowercase_check.grid(row=3, column=0, padx=10, pady=5, sticky='w')

        numbers_check = ttk.Checkbutton(self.master, text="Numbers", variable=self.numbers_check_var, style='TCheckbutton')
        numbers_check.grid(row=4, column=0, padx=10, pady=5, sticky='w')

        special_chars_check = ttk.Checkbutton(self.master, text="Special Characters", variable=self.special_chars_check_var, style='TCheckbutton')
        special_chars_check.grid(row=5, column=0, padx=10, pady=5, sticky='w')


        special_requirements_label = ttk.Label(self.master, text="Special Requirements:", style='TLabel')
        special_requirements_label.grid(row=6, column=0, padx=10, pady=5, sticky='e')

        self.special_requirements_entry = ttk.Entry(self.master, textvariable=tk.StringVar(), width=20, style='TEntry')
        self.special_requirements_entry.grid(row=6, column=1, padx=10, pady=5, sticky='w')


        generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password, style='TButton')
        generate_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.password_label = ttk.Label(self.master, text="", style='TLabel')
        self.password_label.grid(row=8, column=0, columnspan=2, pady=5)

    def generate_password(self):
        length = int(self.length_entry.get())
        uppercase = self.uppercase_check_var.get()
        lowercase = self.lowercase_check_var.get()
        numbers = self.numbers_check_var.get()
        special_chars = self.special_chars_check_var.get()
        special_requirements = self.special_requirements_entry.get()

        password = self._generate_password(length, uppercase, lowercase, numbers, special_chars, special_requirements)
        self.password_label.configure(text="Generated Password: " + password)

    def _generate_password(self, length, uppercase, lowercase, numbers, special_chars, special_requirements):
        chars = ""
        if uppercase:
            chars += string.ascii_uppercase
        if lowercase:
            chars += string.ascii_lowercase
        if numbers:
            chars += string.digits
        if special_chars:
            chars += string.punctuation
        chars += special_requirements

        if not chars:
            return "Please select at least one character type."

        return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
