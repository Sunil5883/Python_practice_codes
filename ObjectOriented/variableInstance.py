class Bank:
    bank_name = 'SBI'
    def __init__(self, name, age, bal):
        self.name= name
        self.age= age
        self.user_balance = bal
    def get_info(self):
        print(f'''User Name: {self.name} and 
        User Balance: {self.user_balance}
        for bank : {self.bank_name}''') # calling of class based variables in method we can use self and Class Name
    

b1 = Bank("Sunil",22,2500)
print(b1.bank_name)
print(Bank.bank_name)
b1.get_info()