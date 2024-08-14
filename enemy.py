from Character import Character

class Enemy(Character):

    def __init__(self, characterHP = 5):
        super().__init__(characterHP)