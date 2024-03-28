from src.view.LoginScreen import LoginScreen
import tkinter as tk
import threading
import time

class Windows:
    def __init__(self):
        self.master = tk.Tk()
        self.master.resizable(False,False)
        self.master.protocol("WM_DELETE_WINDOW",self.quit)
        
        self.thread_flag = True
        self.statut = None
        self.login_screen()
        self.master.mainloop()
    
    def quit(self):
        self.thread_flag = False
        self.master.destroy()
    
    def login_screen(self):
        login_screen = LoginScreen(self.master)
        self.statut = "login"
        
        def check():
            while self.thread_flag:
                if login_screen.statut == "login":
                    self.information = login_screen.information
                    print(self.information)
                    break
                else:
                    print("waiting")
                time.sleep(1)
        threading.Thread(target=check).start()
