class BankAccount:
    bank_name = "dojo bank"
    all_accounts = []

    def __init__(self, int_rate = .01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def witdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("withdrawl succeful")
        
    def display_account(self):
        print("Your balance is  $",self.balance)

    def interest(self):
        if self.balance > 0:
            self.balance * self.int_rate
        print()
account1 = BankAccount()
account2 = BankAccount()

account1.deposit(100).witdraw(50)

account1.display_account()


