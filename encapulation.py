# it restricts access to certain attribut
# and methods to prevent direct modification
class Bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount > 5 and amount <=1000000:
            self.__balance += amount
    def get_balance(self):
        return self.__balance

account=Bankaccount(22000)
account.deposit(3500)
print("balance",account.get_balance())
