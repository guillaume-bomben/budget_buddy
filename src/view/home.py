import tkinter as tk

class Home(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.statut = None
        self.widgets()
        
    def widgets(self):
        frame = tk.Frame(master=self)
        frame.pack()
        
        self.balance_label = tk.Label(master=frame, text="solde : 0")
        self.balance_label.pack()
        
        self.button_logout = tk.Button(master=frame, text="déconnexion", command=self.logout)
        self.button_logout.pack()
        
        self.button_list = tk.Button(master=frame, text="liste operation", command=self.operation_list)
        self.button_list.pack()
        
        self.button_transaction = tk.Button(master=frame, text="transaction", command=self.transaction)
        self.button_transaction.pack()

    def logout(self):
        self.statut = "logout"
    
    def operation_list(self):
        self.statut = "transaction list"

    def transaction(self):
        self.statut = "transaction page"
