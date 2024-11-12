from random import randint
from time import sleep

number = randint(0, 3)

print('Бросаю монетку...')

sleep(1)

if number == 0:
    print('Орел!')
else:
    print('Решка!')
    
