from charachter import Character, Vampire

player_1 = Character(name='Mamont', damage=25)
print(player_1.stats())
player_2 = Vampire(name='Toothnik', hp=70, damage=30)
print(player_2.stats())
