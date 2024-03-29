from src.view.LoginScreen import LoginScreen
from src.view.RegisterScreen import RegisterScreen
from src.view.home import Home
import tkinter as tk
import threading
import time
import os

class Windows:
    def __init__(self):
        self.master = tk.Tk()
        self.master.resizable(False,False)
        self.master.geometry("800x600")
        self.master.protocol("WM_DELETE_WINDOW",self.quit)
        
        self.thread_flag = None
        self.statut = None

    def quit(self):
        self.thread_flag = False
        self.master.destroy()
        os._exit(0)
    
    def login_screen(self):
        self.log_screen = LoginScreen(self.master)
        self.log_screen.pack()
        print("login")
        
        def check():
            self.thread_flag = True
            while self.thread_flag:
                if self.log_screen.statut == "login":
                    self.statut = "login"
                    self.information = self.log_screen.information
                    print(self.information)
                    break
                elif self.log_screen.statut == "register":
                    self.statut = "register"
                    break
                else:
                    print("waiting_1")
                time.sleep(1)
        threading.Thread(target=check).start()

    def forget_login(self):
        self.log_screen.pack_forget()

    def home_page(self):
        self.home = Home(self.master)
        self.home.pack()
        
        def check():
            self.thread_flag = True
            while self.thread_flag:
                if self.home.statut == "logout":
                    self.statut = "logout"
                    break
                elif self.home.statut == "send":
                    self.statut = "send"
                    break
                elif self.home.statut == "recive":
                    self.statut = "recive"
                    break
                else:
                    print("waiting_2")
                time.sleep(1)
        threading.Thread(target=check).start()
    
    def Register_Screen(self):
        
        self.register_screen = RegisterScreen(self.master)
        self.register_screen.pack()
        
        def check():
            self.thread_flag = True
            while self.thread_flag:
                if self.register_screen.statut == "register":
                    self.statut = "register"
                    self.information = self.register_screen.information
                    print(self.information)
                    break
                else:
                    print("waiting_3")
                time.sleep(1)
        threading.Thread(target=check).start()