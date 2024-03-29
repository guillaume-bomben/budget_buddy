import tkinter as tk
from tkinter import messagebox

class LoginScreen(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.statut = None
        self.information = []
        self.widgets()
    
    def widgets(self):
        frame = tk.Frame(master=self)
        frame.pack()
        
        self.label_email = tk.Label(master=frame,text="email")
        self.label_email.pack()
        
        self.entry_email = tk.Entry(master=frame)
        self.entry_email.pack()
        
        self.label_password = tk.Label(master=frame,text="password")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(master=frame,show="*")
        self.entry_password.pack()
        
        self.button_login = tk.Button(master=frame,text="Login",command=self.login)
        self.button_login.pack()
        
        self.register = tk.Button(master=frame,text="Register",command=self.register)
        self.register.pack()
    
    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if email != "" and password != "":
            self.statut = "login"
            self.information = [email,password]
        else:
            tk.messagebox.showerror("Erreur","Veuillez remplir tous les champs")
    
    def register(self):
        self.statut = "register"