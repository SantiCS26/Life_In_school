from Character import Character

class Player(Character):

    def __init__(self, characterHP=10, moneyAmount=0):
        super().__init__(characterHP)
        self.moneyAmount = moneyAmount

    def getMoneyAmount(self):
        return self.moneyAmount

    def add_money(self, moneyAdd):
        self.moneyAmount += moneyAdd

    def remove_money(self, moneyRemove):
        self.moneyAmount -= moneyRemove

    