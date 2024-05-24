#dice_roller.py
# Coded by Amber Shifflett in May 2024
print('Dice Roller by Amber Shifflett')
import random
from time import sleep

random.seed()
a = 0
while a < 5:
    random.randint(0, 10)
    a += 1
    sleep(0.3)

#running = True
#while running:
#    pass
