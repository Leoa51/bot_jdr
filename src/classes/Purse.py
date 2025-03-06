class Purse:

    balance = 0

    def __init__(self, balance = 0):
        self.balance = balance



    def SubtractBalance(self, balance):
        if self.balance >= balance:
            self.balance -= balance
            return True
        else:
            return False