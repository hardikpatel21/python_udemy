"""
This Script is to understand concepts of Opbject oriented Programming and inheritance in python

"""

class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount



    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# example of inheritance
class Checking(Account):
    """This class generates checking account objects"""
    # class variable
    type="checking"
    # you can also create your own instance variables more than than parentas shown below
    def __init__(self,filepath,fee):
        # calling init method of the Account class
        Account.__init__(self, filepath)
        self.fee = fee

    # you can create more method according to the need in your child method
    def tranfer(self,amount):
        self.balance=self.balance - amount - self.fee

checking=Checking("balance.txt", 1)
checking.tranfer(100)
print(checking.balance)
checking.commit()

# use this to see document comments written in """
print(checking.__doc__)
