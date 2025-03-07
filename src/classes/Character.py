from src.classes.Purse import Purse
class Character:

    # purse = Purse()
    # def __init__(self, name, hp):
    #     self.name = name
    #     self.hp = hp
    #     self.current_hp = hp

    def __init__(self, name, hp, current_hp = None, purse = None):
        self.name = name
        self.hp = hp
        self.current_hp = current_hp if current_hp is not None else hp
        self.purse = Purse() if purse is None else Purse(purse)

    def getMoney(self):
        return self.purse.balance


    def heal(self, amount):
        self.current_hp = min(self.current_hp + amount, self.hp)

    def take_damage(self, amount):
        self.current_hp = max(self.current_hp - amount, 0)

    def to_dict(self):
        return {"name": self.name, "hp": self.hp, "current_hp": self.current_hp, "money" : self.getMoney()}