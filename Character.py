class Character:

    def __init__(self, characterHP = 10):
        self.characterHP = characterHP

    def getHP(self):
        return self.characterHP

    def add_health(self, addAmount):
        self.characterHP += addAmount

    def remove_health(self, removeAmount):
        self.characterHP -= removeAmount