#dice_roller.py
# Coded by Amber Shifflett in May 2024
print('Dice Roller by Amber Shifflett')
import sys
import random
from time import sleep

random.seed()
a = 0
while a < 5:
    random.randint(0, 10)
    a += 1
    sleep(0.3)

def roll_die(numSides):
    try:
        numSides = int(numSides)
    except:
        print('Error: not a number')
        sys.exit(1)
    result = random.randint(1, numSides)

#running = True
#while running:
#    pass
