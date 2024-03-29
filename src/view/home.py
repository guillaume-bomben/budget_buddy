import tkinter as tk

class Home(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.statut = None
        self.widgets()
        self.master.mainloop()
        
    def widgets(self):
        frame = tk.Frame(master=self)
        frame.pack()
        
        self.balance_label = tk.Label(master=frame, text="solde : 0")
        self.balance_label.pack()
        
        self.button_logout = tk.Button(master=frame, text="déconnexion", command=self.logout)
        self.button_logout.pack()
        
        self.button_send = tk.Button(master=frame, text="depense", command=self.send)
        self.button_send.pack()
        
        self.button_recive = tk.Button(master=frame, text="revenue", command=self.recive)
        self.button_recive.pack()

    def logout(self):
        self.statut = "logout"
    
    def send(self):
        self.statut = "send"
    
    def recive(self):
        self.statut = "recive"
