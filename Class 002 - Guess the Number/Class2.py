import random

print('=============================================')
print('            Guess that number game')
print('=============================================')
print()

guess = -100
the_number = random.randint(0, 100)

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {}, your guess of {} was too LOW'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH'.format(name, guess))
    else:
        print('You Win!')
print('')
print('')

input('Press any key to Exit')
