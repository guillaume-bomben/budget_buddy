from src.view.LoginScreen import LoginScreen
from src.view.RegisterScreen import RegisterScreen
from src.view.transactionScreen import TransactionScreen
from src.view.ListTransactionScreen import ListTransactionScreen
from src.view.home import Home
import tkinter as tk
import threading
import time
import os


class Windows:
    def __init__(self):
        self.master = tk.Tk()
        self.master.resizable(False,False)
        self.master.protocol("WM_DELETE_WINDOW",self.quit)
        
        self.thread_flag = None
        self.statut = None

    def quit(self):
        self.thread_flag = False
        self.master.destroy()
        os._exit(0)
    
    def login_screen(self):
        self.master.geometry("200x125")

        self.log_screen = LoginScreen(self.master)
        self.log_screen.pack()
        print("login")
        self.thread_flag = True
        def check():
            while self.thread_flag:
                if self.log_screen.statut == "login":
                    self.statut = "login"
                    self.log_screen.statut = None
                    self.information = self.log_screen.information
                    print(self.information)
                    self.thread_flag = False
                elif self.log_screen.statut == "register page":
                    self.log_screen.statut = None
                    self.statut = "register page"
                    self.thread_flag = False
                else:
                    print("waiting_1")
                time.sleep(1)
        threading.Thread(target=check).start()

    def home_page(self,balance):
        self.home = Home(self.master,balance)
        self.home.pack()
        
        def check():
            self.thread_flag = True
            while self.thread_flag:
                if self.home.statut == "logout":
                    self.home.statut = None
                    self.statut = "logout"
                    self.thread_flag = False
                elif self.home.statut == "transaction list":
                    self.home.statut = None
                    self.statut = "transaction list"
                    self.thread_flag = False
                elif self.home.statut == "transaction page":
                    self.home.statut = None
                    self.statut = "transaction page"
                    self.thread_flag = False
                else:
                    print("waiting_2")
                time.sleep(1)
        threading.Thread(target=check).start()
    
    def Register_Screen(self):
        self.master.geometry("200x210")
        self.register_screen = RegisterScreen(self.master)
        self.register_screen.pack()
        
        def check():
            self.thread_flag = True
            while self.thread_flag:
                if self.register_screen.statut == "Create account":
                    self.register_screen.statut = None
                    self.statut = "Create account"
                    self.information = self.register_screen.information
                    print(self.information)
                    self.thread_flag = False
                elif self.register_screen.statut == "login page":
                    self.register_screen.statut = None
                    self.statut = "login page"
                    self.thread_flag = False
                else:
                    print("waiting_3")
                time.sleep(1)
        threading.Thread(target=check).start()
    
    
    def transaction_screen(self,user_list):
        self.transaction_screen = TransactionScreen(self.master,user_list)
        self.transaction_screen.pack()
        
        def check():
            self.thread_flag = True
            while self.thread_flag:
                if self.transaction_screen.statut == "transaction":
                    self.transaction_screen.statut = None
                    self.statut = "transaction"
                    self.information = self.transaction_screen.information
                    print(self.information)
                    self.thread_flag = False
                else:
                    print("waiting_4")
                time.sleep(1)
        threading.Thread(target=check).start()
    
    def list_transaction_screen(self,transactions):
        self.list_transaction_screen = ListTransactionScreen(self.master,transactions)
        self.list_transaction_screen.pack()
        
        def check():
            self.thread_flag = True
            while self.thread_flag:
                if self.list_transaction_screen.statut == "back":
                    self.list_transaction_screen.statut = None
                    self.statut = "back"
                    self.thread_flag = False
                else:
                    print("waiting_5")
                time.sleep(1)
        threading.Thread(target=check).start()