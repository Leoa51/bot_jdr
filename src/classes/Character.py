from src.classes.Purse import Purse
class Character:

    # purse = Purse()
    # def __init__(self, name, hp):
    #     self.name = name
    #     self.hp = hp
    #     self.current_hp = hp

    def __init__(self, name, hp, current_hp = None):
        self.name = name
        self.hp = hp
        self.current_hp = current_hp if current_hp is not None else hp

    def getMoney(self):
        return self.purse.balance

    def soigner(self, amount):
        self.hp += amount

    def take_damage(self, amount):
        self.current_hp -= amount

    def to_dict(self):
        return {"name": self.name, "hp": self.hp, "current_hp": self.current_hp}