import random

print("=============================================")
print("            Guess that number game")
print("=============================================")
print()

guess = "-100"
the_number = random.randint(0, 100)
errortrap = ("I don't know what you mean, please try again.")

while guess != the_number:
    guess_text = input("Guess a number between 0 and 100: ")
    guess = int(guess_text)
    if guess < the_number:
        print('Too Low')
    elif guess > the_number:
        print('Too High')
    else
        print('errortrap')
