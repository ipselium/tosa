# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:03:14 2017

@author: cdesjouy
"""


import numpy as np
import random


def gen_name():
    parts = ['ae', 'di', 'mor', 'fam', 'dar', 'kil', 'glar', 'tres', 'gis']

    name = [random.choice(parts) for i in range(random.randint(2, 3))]
    return ''.join(name).capitalize()


def roll_dice(dices, faces):
    return [random.randint(1, faces) for i in range(dices)]


class Character():

    def __init__(self):
        self.name = ''
        self.joker = 3
        self.life = 20
        self.max_dices = 10
        self.dices = 1
        self.faces_list = [4, 6, 8, 10, 12, 16, 20]
        self.faces = 4
        self.level = 1
        self.magic = 1
        self.max_magic = 1
        self.dead = False

    def pyromancer(self):
        self.dices = 1
        self.faces = 4
        self.magic = 8
        self.max_magic = 8

    def warrior(self):
        self.dices = 1
        self.faces = 12
        self.magic = 1
        self.max_magic = 1

    def hunter(self):
        self.dices = 2
        self.faces = 4
        self.magic = 4
        self.max_magic = 4

    def gen_new_knight(self, level):
        self.dices = min(self.max_dices, int(np.ceil(level/5)))   # Add 1 dice every 5 levels until max_dices
        min_faces = min(6, int(np.ceil(level/8)) - 1)
        self.faces = random.choice(self.faces_list[min_faces:min_faces+2])
        self.life = level + random.randint(1, 6*int(np.ceil(level/5)))       # Random (level) (6 + level)
        self.name = gen_name()

    def strike(self):
        return roll_dice(self.dices, self.faces)

    def refill(self):
        self.magic = self.max_magic
        self.joker += 1

    def upgrade(self, N):

        print("You've done a nice job ! A small level {} reward for you ;)".format(self.level))

        if self.dices == self.max_dices and self.faces == self.faces_list[-1]:
            msg = 'Upgrade [l]ife, [j]oker ? '
        elif self.dices == self.max_dices:
            msg = 'Upgrade [f]aces, [l]ife, [j]oker ? '
        elif self.faces == self.faces_list[-1]:
            msg = 'Upgrade [d]ices, [l]ife, [j]oker ? '
        else:
            msg = 'Upgrade [d]ices, [f]aces, [l]ife, [j]oker ? '

        while True:
            what = input(msg)
            if what == 'd' and self.dices <= self.max_dices:
                self.dices += N
                print('\t ==> +{} dice !'.format(N))
                break
            elif what == 'f' and self.faces < self.faces_list[-N]:
                actual = self.faces_list.index(self.faces)
                self.faces = self.faces_list[actual+N]
                print('\t ==> You have now {} faces !'.format(self.faces))
                break
            elif what == 'l':
                print('\t ==> +{} life !'.format(10*N))
                self.life += 10*N
                break
            elif what == 'j':
                print('\t ==> +{} joker !'.format(int(np.ceil(N/2))))
                self.joker += int(np.ceil(N/2))
                break
            else:
                print('Wrong choice !')

    def stats(self):
        tmp = "\t {:^5} : {:^15} :"      # Used ^ to center text

        print(tmp.format("", self.name))
        print(tmp.format("Dices", self.dices))
        print(tmp.format("Faces", self.faces))
        print(tmp.format("Life", self.life))
