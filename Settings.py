difficulty = {
        "Easy": {
            "enemyHitMultiplier": 0.5,
        },
        "Medium": {
            "enemyHitMultiplier": 1.0
        },
        "Hard": {
            "enemyHitMultiplier": 1.5
        }
    }

class Settings:
    
    def __init__(self, difficultySelected="Medium", playerName="Name") -> None:
        self.difficulty_Selected = difficultySelected
        self.playerName = playerName



    def set_Difficulty(self, difficultyChosen):
        self.difficulty_Selected = difficultyChosen

    def test_Selection(self):
        print(self.difficulty_Selected)

    def set_name(self, playerNameChosen):
        self.playerName = playerNameChosen

    def test_name(self):
        print(self.playerName)