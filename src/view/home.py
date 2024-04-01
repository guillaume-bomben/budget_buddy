import tkinter as tk

class Home(tk.Frame):
    def __init__(self, master,balance):
        super().__init__(master)

        self.balance = balance
        self.statut = None
        self.widgets()
        
    def widgets(self):
        frame = tk.Frame(master=self)
        frame.pack()
        
        self.header_frame = tk.Frame(master=frame)
        self.header_frame.pack()
        
        self.balance_label = tk.Label(self.header_frame, text=f"SOLDE : {self.balance}", font=("Arial", 15))
        self.balance_label.grid(row=0, column=0, padx=30)
        
        self.button_logout = tk.Button(self.header_frame, text="déconnexion", command=self.logout)
        self.button_logout.grid(row=0, column=1, padx=10)
        
        self.button_list = tk.Button(self.header_frame, text="liste operation", command=self.operation_list)
        self.button_list.grid(row=0, column=2, padx=10)
        
        self.button_transaction = tk.Button(self.header_frame, text="transaction", command=self.transaction)
        self.button_transaction.grid(row=0, column=3, padx=10)

    def logout(self):
        self.statut = "login page"
    
    def operation_list(self):
        self.statut = "transaction list"

    def transaction(self):
        self.statut = "transaction page"
