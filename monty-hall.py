# The Monty Hall Problem

import random

# Instantiating a random treasure map
def single_run():
    maps = ['wasteland', 'wasteland', 'wasteland']
    treasure_index = random.randint(0, 2)
    maps[treasure_index] = 'one piece'
    return maps

# Luffy's first choice
def luffy():
    luffy_first_choice = random.randint(0, 2)
    return luffy_first_choice

# Monty's choice of a location that is neither Luffy's choice nor the treasure location
def monty(maps, luffy_first_choice):
    monty_choice = 0

    while monty_choice == luffy_first_choice or maps[monty_choice] == 'one piece':
        monty_choice += 1
    
    return monty_choice

# switch Luffy's choice
def luffy_switch(luffy_first_choice, monty_choice):
    
    luffy_switch_choice = 0

    while luffy_switch_choice == luffy_first_choice or luffy_switch_choice == monty_choice:
        luffy_switch_choice += 1

    return luffy_switch_choice

# output to be displayed
def output(stick, switch, trials):
    stick_percent = round((stick/trials) * 100)
    switch_percent = round((switch/trials) * 100)
    
    print(f'Luffy found One Piece {stick_percent} % of the time when he decided to stick to his initial choice ')
    print(f'Luffy found One Piece {switch_percent} % of the time when he decided to switch his initial choice')


print('The Monty Hall Problem')
trials = int(input('Enter the number of trials:  '))

# Luffy sticks
stick_count = 0

# Luffy switches
switch_count = 0

for i in range(trials):
    maps = single_run()
    luffy_first_choice = luffy()
    monty_choice = monty(maps, luffy_first_choice)
    luffy_switch_choice = luffy_switch(luffy_first_choice, monty_choice)

    if maps[luffy_first_choice] == 'one piece':
        stick_count += 1
    
    elif maps[luffy_switch_choice] == 'one piece':
        switch_count += 1

output(stick_count, switch_count, trials) 

 