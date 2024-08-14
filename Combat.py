class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def attack(self, attacker, defender):
        damage = 1 
        defender.remove_health(damage)
        return damage

    def player_attack(self):
        return self.attack(self.player, self.enemy)

    def enemy_attack(self):
        print("Enemy attack: " + str(self.enemy.getHP()))
        return self.attack(self.enemy, self.player)

    def is_battle_over(self):
        return self.player.getHP() <= 0 or self.enemy.getHP() <= 0