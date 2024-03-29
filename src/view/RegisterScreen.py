import tkinter as tk
from tkinter import messagebox

class RegisterScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.statut = None
        self.information = []
        self.widgets()

    def widgets(self):
        frame = tk.Frame(master=self)
        frame.pack()
        
        self.label_first_name = tk.Label(master=frame, text="Nom")
        self.label_first_name.pack()
        
        self.entry_first_name = tk.Entry(master=frame)
        self.entry_first_name.pack()
        
        self.label_last_name = tk.Label(master=frame, text="Prénom")
        self.label_last_name.pack()
        
        self.entry_last_name = tk.Entry(master=frame)
        self.entry_last_name.pack()
        
        self.label_email = tk.Label(master=frame, text="Email")
        self.label_email.pack()
        
        self.entry_email = tk.Entry(master=frame)
        self.entry_email.pack()
        
        self.label_password = tk.Label(master=frame, text="Password")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(master=frame, show="*")
        self.entry_password.pack()
        
        self.button_register = tk.Button(master=frame, text="Register", command=self.register)
        self.button_register.pack()
        
        self.login = tk.Button(master=frame, text="Login", command=self.login)
        self.login.pack()

    def register(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if username != "" and email != "" and password != "":
            self.statut = "register"
            self.information = [username, email, password]
        else:
            tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs")

    def login(self):
        self.statut = "login"