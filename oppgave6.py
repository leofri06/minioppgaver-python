import random

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False


Character1 = Character("Character A", 100)
Character2 = Character("Character B", 100)

for x in range(3):
    damage = random.randint(20, 50)
    print(f"\nRunde {x + 1}:")
    print(f"{Character1.name} angriper {Character2.name} for {damage} skade.")
    Character2.take_damage(damage)
    if not Character2.is_alive():
        print(f"{Character2.name} er beseiret!")
        break
    print(f"{Character2.name} har {Character2.hp} HP igjen.")
