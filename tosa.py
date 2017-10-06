# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:58:55 2017

TODO :
    * Ennemi can drop item :
        * weapon to increase faces
        * shield to gain armor ?
    * Spells :
        * Ice : ennemi takes some damages and is frozen (can't attack next turn)
    * Quit game (with state save)
@author: cdesjouy
"""


import time
import os


from kombat import Kombat
from character import Character


def rules():
    _ = os.system('clear')
    print(80*'#')
    print('# {:^76} #'.format('The Ogress Super Adventure !'))
    print(80*'#' + '\n')
    print(80*'#')
    print('# {:76} #'.format('This is an adventure game in which you are an ogress tryng to rescue'))
    print('# {:76} #'.format('his sweet lovely ogre. You will successively fight knights to go up at'))
    print('# {:76} #'.format('the top of the dungeon where you lover is captive !'))
    print('# {:76} #'.format('For each fight you have several options: '))
    print('# {:76} #'.format('  -Fight  : Roll X Z-faces dices and try to kill the knight'))
    print('# {:76} #'.format('  -Escape : Try to escape, but the knight can hit you in the back !'))
    print('# {:76} #'.format('  -Joker  : Sneak in the back of the knight and assassinate him'))
    print('# {:76} #'.format('  -Spell  : Launch a fireball with power Z*[1-4] (faces)'))
    print(80*'#' + '\n')
    _ = input('\nPress enter to start the adventure ...')


def char_select():
    _ = os.system('clear')
    print(80*'#')
    print('# {:^76} #'.format('The Ogress Super Adventure !'))
    print(80*'#' + '\n')
    print(80*'#')
    print('# {:76} #'.format('You first have to select a class of character :'))
    print('# {:76} #'.format('  - (1) Warrior    : Brutal force !'))
    print('# {:76} #'.format('  - (2) Hunter     : Fast and Mytic !'))
    print('# {:76} #'.format('  - (3) Pyromancer : Deeply Mystic !'))
    print(80*'#' + '\n')

    you = Character()
    while True:
        select = input('\nWhich class (1, 2, or 3) ? ')
        print(select)
        if select == '1':
            you.warrior()
            break
        elif select == '2':
            you.hunter()
            break
        elif select == '3':
            you.pyromancer()
            break
    return you

if __name__ == "__main__":

    # Rules
    rules()

    # Initial values
    you = char_select()

    while not you.dead:

        # Clear screen
        _ = os.system('clear')

        # Characters
        him = Character()
        him.gen_new_knight(you.level)

        # Rewards
        if you.level % 5 == 0 and you.level % 10 != 0:
            you.upgrade(1)
            time.sleep(2)
            _ = os.system('clear')

        if you.level % 10 == 0:
            you.upgrade(2)
            you.refill()
            time.sleep(2)
            _ = os.system('clear')

        # Kombat
        Kombat(you, him)

        if him.dead and not you.dead:
            you.level += 1
            print('\nGo to level {} ...'.format(you.level))

        time.sleep(2)

    print(80*'#')
    print('# {:^76} #'.format('Game Over'))
    print(80*'#')
