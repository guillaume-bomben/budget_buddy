import tkinter as tk

class LoginScreen:
    def __init__(self,master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")
        
        self.statut = None
        self.information = []
        self.widgets()
    
    def widgets(self):
        self.label_email = tk.Label(self.master,text="email")
        self.label_email.pack()
        
        self.entry_email = tk.Entry(self.master)
        self.entry_email.pack()
        
        self.label_password = tk.Label(self.master,text="password")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(self.master,show="*")
        self.entry_password.pack()
        
        self.button_login = tk.Button(self.master,text="Login",command=self.login)
        self.button_login.pack()
        
        self.register = tk.Button(self.master,text="Register",command=self.register)
        self.register.pack()
    
    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if email != "" and password != "":
            self.statut = "login"
            self.information = [email,password]
    
    def register(self):
        self.statut = "register"