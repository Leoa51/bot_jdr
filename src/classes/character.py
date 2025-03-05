class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def soigner(self, amount):
        self.hp += amount

    def subir_dommage(self, amount):
        self.hp -= amount

    def to_dict(self):
        return {"name": self.name, "hp": self.hp}