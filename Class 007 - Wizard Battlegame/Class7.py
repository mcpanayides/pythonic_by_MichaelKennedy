from actors import Wizard, Creature, SmallAnimal, Dragon
import random, time

def main():
    print_header()
    game_loop()

def print_header():
    print('==========================')
    print('|       Wizard App       |')
    print('==========================')
    print()

def game_loop():

    creatures = [SmallAnimal('Toad', 1),
                 SmallAnimal('Bat', 3),
                 Creature('Tiger', 12),
                 Dragon('Dragon', 50, 75, True),
                 Wizard('Evil Wizard', 100),
                ]
    
    hero = Wizard('Gandalf', 75)


    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared, from a dark foggy forest...'.format(active_creature.name, active_creature.level))
        print()
        
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around, or [q]uit?')
       
        if cmd == 'a':
            knockedOut = random.randint(1, 10)
            
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The Wizard collapsed, please wait for him to recover for {} seconds'.format(knockedOut))
                time.sleep(knockedOut)
                print('The Wizard awakens')
                print()

        elif cmd == 'r':
            print('runaway')
            
        elif cmd == 'l':
            print('The wizard {} looks around:'.format(hero.name))
            for creature in creatures:
                print('* A {} of level {}'.format(creature.name, creature.level))

        elif cmd == 'q':
            print('Ok, Exiting')
            break
            
        else:
            print('Sorry thats unknown try again')

        if not creatures:
            print('')
            print('Congrat you beat all the creatures!')
            break
 

if __name__ == '__main__':
    main()
