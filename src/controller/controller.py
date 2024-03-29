from src.Model.Database.user import User
from src.Model.Database.transaction import transaction
from src.view.Windows import Windows
import threading
import tkinter as tk
from tkinter import messagebox

class controller:
    def __init__(self):
        self.user = User()
        self.transaction = transaction()
        self.windows = Windows()
        self.windows.master.protocol("WM_DELETE_WINDOW",self.windows.quit)
        
        self.windows.login_screen()
        threading.Thread(target=self.change_page_logic).start()
        self.windows.master.mainloop()

    def login(self,email,password):
        if self.user.get_id(email,password):
            self.windows.log_screen.pack_forget()
            self.windows.home_page()
        else:
            self.windows.master.messagebox.showerror("Erreur","Email ou mot de passe incorrect")

    def login_to_register(self):
        self.windows.forget_login()
        self.windows.Register_Screen()

    def register_to_login(self):
        self.windows.register_screen.pack_forget()
        self.windows.login_screen()

    def register(self,lastname,firstname,email,password,balance):
        if type(self.user.verify_email(email)[0]) != int:
            self.windows.master.messagebox.showerror("Erreur","Cette Email est deja utilisé")
        else:
            self.user.create(lastname,firstname,email,password,balance)
            self.windows.register_screen.pack_forget()
            self.windows.login_screen()
            
    
    def change_page_logic(self):
        running = True
        while running:
            if self.windows.statut == "register":
                self.login_to_register()
                running = False
            elif self.windows.statut == "login":
                self.login(self.windows.information[0],self.windows.information[1])
                running = False