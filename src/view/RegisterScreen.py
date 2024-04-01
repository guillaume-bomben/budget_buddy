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
        
        self.label_password = tk.Label(master=frame, text="mot de passe")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(master=frame, show="*")
        self.entry_password.pack()
        
        self.button_frame = tk.Frame(master=frame)
        self.button_frame.pack(pady=10)
        
        self.button_register = tk.Button(self.button_frame, text="Inscription", command=self.register)
        self.button_register.grid(row=0, column=0, padx=5)
        
        self.button_login = tk.Button(self.button_frame, text="Conexion", command=self.login)
        self.button_login.grid(row=0, column=1, padx=5)

    def register(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if first_name != "" and last_name != "" and email != "" and password != "":
            self.statut = "Create account"
            self.information = [first_name,last_name, email, password]
        else:
            tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs")

    def login(self):
        self.statut = "login page"