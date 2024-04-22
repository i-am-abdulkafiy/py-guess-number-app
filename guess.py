'''Guessing Number App'''
#Importing Random Module
import random

#Render a variable to assign value to (maximum_number)
maximum_number = 200

#Using random.randint
number = random.randint(1, maximum_number)

#Setting guess value to none
guess = None

#Using iteration (while)
while guess != number:
    guess = int(input('Key in any number: '))
    if guess < number:
        print('Number too small')
    if guess > number:
        print('Number\'s too large')
        print('Congrats!, you\'re now a great number guesser.')
        break
