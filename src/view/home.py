import tkinter as tk

class Home(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Home")
        self.master.geometry("400x400")

        self.statut = None
        self.widgets()
        self.master.mainloop()
        
    def widgets(self):
        self.balance_label = tk.Label(self.master, text="solde : 0")
        self.balance_label.pack()
        
        self.button_logout = tk.Button(self.master, text="déconnexion", command=self.logout)
        self.button_logout.pack()
        
        self.button_send = tk.Button(self.master, text="depense", command=self.send)
        self.button_send.pack()
        
        self.button_recive = tk.Button(self.master, text="revenue", command=self.recive)
        self.button_recive.pack()

    def logout(self):
        self.statut = "logout"
    
    def send(self):
        self.statut = "send"
    
    def recive(self):
        self.statut = "recive"
