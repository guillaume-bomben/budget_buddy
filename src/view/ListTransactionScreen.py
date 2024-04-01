import tkinter as tk
from tkinter import ttk

class ListTransactionScreen(tk.Frame):
    def __init__(self, master, transactions):
        super().__init__(master)
        self.statut = None
        self.transactions = transactions
        print(self.transactions)
        self.widgets()
    
    def widgets(self):
        frame = tk.Frame(master=self)
        frame.pack()
        
        self.list_transaction = ttk.Treeview(frame, columns=("envoyer", "destinataire", "description", "montant", "type"), show="headings")
        self.list_transaction.heading("envoyer", text="Envoyer")
        self.list_transaction.heading("destinataire", text="Destinataire")
        self.list_transaction.heading("description", text="Description")
        self.list_transaction.heading("montant", text="Montant")
        self.list_transaction.heading("type", text="Type")
        
        self.list_transaction.column("envoyer", width=50)
        self.list_transaction.column("destinataire", width=50)
        self.list_transaction.column("description", width=150)
        self.list_transaction.column("montant", width=50)
        self.list_transaction.column("type", width=75)
        
        self.list_transaction.pack()
        
        for transaction in self.transactions:
            self.list_transaction.insert("", "end", values=(transaction[0], transaction[1], transaction[2], transaction[3], transaction[4]))
        
        self.button_back = tk.Button(master=frame, text="Retour", command=self.back)
        self.button_back.pack()
    
    def back(self):
        self.statut = "home page"