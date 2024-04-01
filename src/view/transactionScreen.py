import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TransactionScreen(tk.Frame):
    def __init__(self, master,user_list):
        super().__init__(master)
        self.user_list = user_list
        
        self.statut = None
        self.information = []
        self.widgets()

    def widgets(self):
        frame = tk.Frame(master=self)
        frame.pack()
        
        self.label_type = tk.Label(master=frame, text="Type de transaction")
        self.label_type.pack()
        
        self.entry_type = ttk.Combobox(master=frame, values=["depot","retrait","virement"])
        self.entry_type.pack()
        
        self.label_amount = tk.Label(master=frame, text="Montant")
        self.label_amount.pack()
        
        self.entry_amount = tk.Entry(master=frame)
        self.entry_amount.pack()
        
        def widgetPlus():
            while True:
                if self.entry_type.get() == "virement":
                    self.label_user = tk.Label(master=frame, text="destinataire")
                    self.label_user.pack()
                    
                    self.entry_user = ttk.Combobox(master=frame, values=self.user_list)
                    self.entry_user.pack()
                    
                    self.label_description = tk.Label(master=frame, text="Description")
                    self.label_description.pack()
                    
                    self.entry_description = tk.Entry(master=frame)
                    self.entry_description.pack()
                    break
        threading.Thread(target=widgetPlus).start()
        
        self.button_transaction = tk.Button(master=frame, text="Transaction", command=self.transaction)
        self.button_transaction.pack()
    
    def transaction(self):
        type = self.entry_type.get()
        amount = self.entry_amount.get()
        
        if type == "virement":
            user = self.entry_user.get().split(" ")[0]
            description = self.entry_description.get()
            if amount != "" and user != "" and description != "":
                self.statut = "transaction"
                self.information = [type,amount,user,description]
            else:
                tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
        elif type != "" and amount != "":
            self.statut = "transaction"
            self.information = [type,amount]
        else:
            tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
            