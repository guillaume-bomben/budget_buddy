from src.Model.Database.user import User
from src.Model.Database.transaction import transaction
from src.view.Windows import Windows

class controller:
    def __init__(self):
        self.user = User()
        self.transaction = transaction()
        self.windows = Windows()
        
        self.windows.login_screen()
