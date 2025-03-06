from src.classes.Purse import Purse
class Character:

    # purse = Purse()

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def getMoney(self):
        return self.purse.balance

    def soigner(self, amount):
        self.hp += amount

    def subir_dommage(self, amount):
        self.hp -= amount

    def to_dict(self):
        return {"name": self.name, "hp": self.hp}