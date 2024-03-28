import tkinter as tk

class RegisterScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Register")
        self.master.geometry("300x250")
        
        self.status = None
        self.information = []
        self.widgets()

    def widgets(self):
        self.label_first_name = tk.Label(self.master, text="Nom")
        self.label_first_name.pack()
        
        self.entry_first_name = tk.Entry(self.master)
        self.entry_first_name.pack()
        
        self.label_last_name = tk.Label(self.master, text="Prénom")
        self.label_last_name.pack()
        
        self.entry_last_name = tk.Entry(self.master)
        self.entry_last_name.pack()
        
        self.label_email = tk.Label(self.master, text="Email")
        self.label_email.pack()
        
        self.entry_email = tk.Entry(self.master)
        self.entry_email.pack()
        
        self.label_password = tk.Label(self.master, text="Password")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack()
        
        self.button_register = tk.Button(self.master, text="Register", command=self.register)
        self.button_register.pack()
        
        self.login = tk.Button(self.master, text="Login", command=self.login)
        self.login.pack()

    def register(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if username != "" and email != "" and password != "":
            self.status = "register"
            self.information = [username, email, password]
        else:
            tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs")

    def login(self):
        self.status = "login"