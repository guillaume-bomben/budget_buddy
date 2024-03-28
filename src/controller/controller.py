from src.Model.Database.user import User
from src.Model.Database.transaction import transaction
from src.view.Windows import Windows
from tkinter import messagebox

class controller:
    def __init__(self):
        self.user = User()
        self.transaction = transaction()
        self.windows = Windows()
        
        self.windows.login_screen()
        self.windows.master.mainloop()

    def login(self,email,password):
        if self.user.get_id(email,password):
            self.windows.master.unpack()
            self.windows.home_page()
        else:
            self.windows.master.messagebox.showerror("Erreur","Email ou mot de passe incorrect")

    def login_to_register(self):
        self.windows.master.unpack()
        self.windows.Register_Screen()

    def register_to_login(self):
        self.windows.master.unpack()
        self.windows.login_screen()

    def register(self,lastname,firstname,email,password,balance):
        if type(self.user.verify_email(email)[0]) != int:
            self.windows.master.messagebox.showerror("Erreur","Cette Email est deja utilisé")
        else:
            self.user.create(lastname,firstname,email,password,balance)
            self.windows.master.unpack()
            self.windows.login_screen()