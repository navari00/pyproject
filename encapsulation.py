# it restrict access to certain attributes and
# methods to prevent direct modification
class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount > 0:
          self.__balance += amount

account=bankaccount(2500)
account.deposit(350)
print("balance",account.get_balance())