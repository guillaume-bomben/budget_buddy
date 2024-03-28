import tkinter as tk

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.root.geometry("400x400")

        self.statut = None
        self.widgets()
        self.root.mainloop()
        
    def widgets(self):
        self.balance_label = tk.Label(self.root, text="solde : 0")
        self.balance_label.pack()
        
        self.button_logout = tk.Button(self.root, text="déconnexion", command=self.logout)
        self.button_logout.pack()
        
        self.button_send = tk.Button(self.root, text="depense", command=self.send)
        self.button_send.pack()
        
        self.button_recive = tk.Button(self.root, text="revenue", command=self.recive)
        self.button_recive.pack()

    def logout(self):
        self.statut = "logout"
    
    def send(self):
        self.statut = "send"
    
    def recive(self):
        self.statut = "recive"
