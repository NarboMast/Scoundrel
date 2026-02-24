class Weapon:
    def __init__(self, damage, last_enemy_rank):
        self.damage = damage
        self.last_enemy_rank = last_enemy_rank

    def __repr__(self):
        return f'Damage: {self.damage}, Last enemy rank: {self.last_enemy_rank}'