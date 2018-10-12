import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} level: {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level    
        
    def attack(self, Creature):
        print('The wizard {} attacks {}!'.format(self.name, Creature.name))
        player_roll = self.get_defensive_roll()
        #creature_roll = random.randint(1, 12) * self.level
        creature_roll = Creature.get_defensive_roll()
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

class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness
    
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_mod = 5 if self.breaths_fire else 1
        scale_mod = self.scaliness / 10
        return base_roll * fire_mod * scale_mod