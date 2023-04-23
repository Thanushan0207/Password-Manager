import tkinter as tk
from tkinter import simpledialog
import hashlib

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.passwords = {}
        
        self.master.title("Password Manager")
        
        self.label = tk.Label(self.master, text="Password Manager", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.add_password_button = tk.Button(self.master, text="Add Password", command=self.add_password)
        self.add_password_button.pack()
        
        self.get_password_button = tk.Button(self.master, text="Get Password", command=self.get_password)
        self.get_password_button.pack()
        
    def add_password(self):
        site = simpledialog.askstring("Add Password", "Enter site name:")
        password = simpledialog.askstring("Add Password", "Enter password:", show="*")
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.passwords[site] = password_hash
        
    def get_password(self):
        site = simpledialog.askstring("Get Password", "Enter site name:")
        if site in self.passwords:
            print("Password for '{}' is '{}'".format(site, self.passwords[site]))
        else:
            print("No password found for '{}'".format(site))

root = tk.Tk()
app = PasswordManager(root)
root.mainloop()