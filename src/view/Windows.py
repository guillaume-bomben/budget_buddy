from view.LoginScreen import LoginScreen
import tkinter as tk

class Windows:
    def __init__(self) -> None:
        self.master = tk.Tk()
        self.master.resizable(False,False)
        
        self.master.mainloop()