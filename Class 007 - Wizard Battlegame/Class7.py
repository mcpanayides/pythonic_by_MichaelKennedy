from actors import Wizard, Creature
import random

def main():
    print_header()
    game_loop()

def print_header():
    print('==========================')
    print('|       Wizard App       |')
    print('==========================')
    print()

def game_loop():

    creatures = [Creature('Toad', 1),
                 Creature('Bat', 3),
                 Creature('Tiger', 12),
                 Creature('Dragon', 50),
                 Creature('Evil Wizard', 1000),
                ]
    
    hero = Wizard('Gandalf', 75)


    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared, from a dark foggy forest...'.format(active_creature.name, active_creature.level))
        print()
        
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            hero.attack(active_creature)
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('lookaround')
        elif cmd == 'q':
            print('Ok, Exiting')
            break
        else:
            print('Sorry thats unknown try again')



if __name__ == '__main__':
    main()
