class User:
    def __init__(self, make_deposit, make_withdrawal, display_balance):
            print (f'User has deposited {make_deposit}')
            self.make_deposit = make_deposit
            self.make_withdrawal = make_withdrawal
            self.display_balance = display_balance
    
    def withdrawal(self):
        print (f'User has withdrawn {self.make_withdrawal}')

    def balance(self):
        print (f'your balance is {self.display_balance}')
        

    
person1= User('$1000,$1000,$1000' , '$400', '$2600')
person2= User('$2000,$2000' , '$1,$1', '$5998')

person1.withdrawal()

person1.balance()


person2.withdrawal()

person2.balance()