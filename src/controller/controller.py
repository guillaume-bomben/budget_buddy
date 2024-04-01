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
        
        self.id_user = None
        
        self.windows.login_screen()
        threading.Thread(target=self.change_page_logic).start()
        self.windows.master.mainloop()

    def login(self,email,password):
        if self.user.get_id(email,password):
            self.id_user = self.user.get_id(email,password)[0][0]
            print(self.id_user)
            self.windows.log_screen.pack_forget()
            self.windows.home_page()
        else:
            tk.messagebox.showerror("Erreur","Email ou mot de passe incorrect")
            self.running = True
            self.windows.thread_flag = True

    def login_to_register(self):
        self.windows.log_screen.pack_forget()
        self.windows.Register_Screen()

    def register_to_login(self):
        self.windows.register_screen.pack_forget()
        self.windows.login_screen()
    
    def home_to_transaction(self):
        self.windows.home.pack_forget()
        self.windows.transaction_screen(self.user.user_list)
    
    def home_to_operation_list(self):
        self.windows.home.pack_forget()
        transaction_list = self.transaction.get_transaction_list(self.id_user)
        new_transaction_list = []
        print(transaction_list)
        for i in range(len(transaction_list)):
            print(self.user.get_user(transaction_list[i][1])[0][1])
            user_send = self.user.get_user(transaction_list[i][0])[0][1]
            user_recive = self.user.get_user(transaction_list[i][1])[0][1]
            new_transaction_list.append([user_send,user_recive,transaction_list[i][2],transaction_list[i][3],transaction_list[i][4]])
        self.windows.list_transaction_screen(new_transaction_list)

    def register(self,lastname,firstname,email,password):
        if self.user.verify_email(email) != []:
            tk.messagebox.showerror("Erreur","Cette Email est deja utilisé")
            self.running = True
            self.windows.thread_flag = True
        else:
            self.user.create(lastname,firstname,email,password,0)
            self.windows.register_screen.pack_forget()
            self.windows.login_screen()
            
    
    def change_page_logic(self):
        self.running = True
        while self.running:
            if self.windows.statut == "register":
                self.windows.statut = None
                self.login_to_register()
            elif self.windows.statut == "login":
                self.windows.statut = None
                self.login(self.windows.information[0],self.windows.information[1])
            elif self.windows.statut == "Create account":
                self.windows.statut = None
                print(self.windows.information)
                self.register(self.windows.information[0],self.windows.information[1],self.windows.information[2],self.windows.information[3])
            elif self.windows.statut == "transaction page":
                self.windows.statut = None
                self.home_to_transaction()
            elif self.windows.statut == "transaction":
                self.windows.statut = None
                if self.windows.information[0] == "virement":
                    self.transaction.create(self.id_user,self.windows.information[2],self.windows.information[3],self.windows.information[1],self.windows.information[0])
                    self.user.update_balance(self.id_user,self.user.get_balance(self.id_user)-self.windows.information[1])
                    self.user.update_balance(self.windows.information[2],self.user.get_balance(self.windows.information[2])+self.windows.information[1])
                else:
                    self.transaction.create(self.id_user,self.id_user,"",self.windows.information[1],self.windows.information[0])
                    if self.windows.information[0] == "depot":
                        self.user.update_balance(self.id_user,self.user.get_balance(self.id_user)+self.windows.information[1])
                    else:
                        self.user.update_balance(self.id_user,self.user.get_balance(self.id_user)-self.windows.information[1])
            elif self.windows.statut == "transaction list":
                self.windows.statut = None
                self.home_to_operation_list()