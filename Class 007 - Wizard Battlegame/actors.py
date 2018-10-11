import random

class Wizard:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level    
    def attack(self, Creature):
        print('The wizard {} attacks {}!'.format(self.name, Creature.name))
        player_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * self.level
        print('{} rolls {}'.format(self.name, player_roll))
        print('{} rolls {}'.format(Creature.name, creature_roll))

        if player_roll >= creature_roll:
            print('The wizard beats {}'.format(Creature.name))
            print()
            return True
        else:
            print('The Wizard was DEFEATED')
            print()
            return False

class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} level: {}".format(self.name, self.level)