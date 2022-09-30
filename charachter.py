class Character:
    def __init__(self, name='', hp=100, damage=25, armor=0):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def attack(self, target):
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.hp = max(self.hp - abs(damage), 0)

    def take_heal(self, heal):
        self.hp = min(self.hp + abs(heal), self.max_hp)

    def stats(self):
        return \
            f' === {self.name} ===\n' \
            f' Здоровье: {self.hp} / {self.max_hp}\n' \
            f' Урон: {self.damage}\n' \
            f' Броня: {self.armor}\n'


class Vampire(Character):
    def __init__(self, name='', hp=70, damage=30, armor=0):
        Character.__init__(self, name, hp, damage, armor)
        self.max_hp = self.hp

    def attack(self, target):
        damage = self.damage()
        target.take_damage(damage)
        self.hp += (self.damage / 10)