# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:00:25 2017

@author: cdesjouy
"""


import random


class Kombat():

    def __init__(self, you, him):
        self.you = you
        self.him = him

        self.stats()

        self.round = 1
        self.action = False
        self.choice()

    def choice(self):

        while True:

            if self.you.dead or self.him.dead:
                break

            self.action = False
            while self.action not in ['e', 'j', 'f', 's']:
                self.action = input('\n\t[f]ight, [e]scape, [j]oker, [s]pell ? ')

            self.dispatch()

    def dispatch(self):

        if self.action == 'e':
            self.escape()
            self.him.dead = True
            if self.you.life < 1:
                self.you.dead = True

        elif self.action == 'j' and self.you.joker > 0:
            self.use_joker()
            self.him.dead = True

        elif self.action == 'j' and self.you.joker == 0:
            print('\n\tNo more jokers ! You have to fight or escape!')

        elif self.action == 'f':
            self.fight()

        elif self.action == 's' and self.you.magic > 0:
            self.fireball()

        elif self.action == 's' and self.you.magic == 0:
            print('\n\tNo more magic !')

    def use_joker(self):
        self.you.joker -= 1
        print('\nYou deal a lethal blow to the Knight {}'.format(self.him.name))
        print('{} jokers left'.format(self.you.joker))

    def escape(self):
        hit = random.randint(0, 3)
        if hit == 0:
            print('\nThe knight did not see you. You succefully sneak in the upstairs!')
        else:
            strike = random.randint(1, self.him.faces*2)
            self.you.life -= strike
            print('\nYou tried to sneak in the upstairs, but the knight hit your back ! You loose {} life'.format(strike))

    def fireball(self):
        strike = random.randint(1, 4)*self.you.faces
        self.him.life -= strike
        print('\n\tYou launch a super spell on the knight. He loses {}  life\n'.format(strike))
        self.you.magic -= 1
        if self.him.life < 1:
            print('\t\tYeahhh ! You killed the knight {}!'.format(self.him.name))
            self.him.dead = True
        else:
            print('\t\tThe knight {} has now {} life left!'.format(self.him.name, self.him.life))

    def fight(self):

        tmp_fight = "\t{:3} : roll {:2} {:2} faces dices => got {} ===> {:3} strike !"
        print('\n\tRound {} : 3, 2, 1, .... FIGHT !\n'.format(self.round))

        strike = self.you.strike()
        print(tmp_fight.format("You", self.you.dices, self.you.faces, strike, sum(strike)))
        self.him.life -= sum(strike)
        if self.him.life > 0:
            strike = self.him.strike()
            print("\t\t==> Knight {} has {} life left".format(self.him.name, self.him.life))
            print(tmp_fight.format('Him', self.him.dices, self.him.faces, strike, sum(strike)))
            self.you.life -= sum(strike)
            print("\t\t==> You have {} life left".format(self.you.life))

        if self.him.life < 1:
            print('\t\tYeahhh ! You killed the knight {}!'.format(self.him.name))
            self.him.dead = True

        elif self.you.life < 1:
            self.you.dead = True

        else:
            self.round += 1

    def stats(self):
        tmp = "\t {:^5} : {:^5} : {:^5} :"      # Used ^ to center text
        print(80*'#')
        level_txt = '# Level {} : you face knight {}'.format(self.you.level, self.him.name)
        stats_txt = 'M:{}/J:{} #'.format(self.you.magic, self.you.joker).rjust(80-len(level_txt))
        print(level_txt + stats_txt)
        print(80*'#')

        print(tmp.format("", "You", "Him"))
        print(tmp.format("Dices", self.you.dices, self.him.dices))
        print(tmp.format("Faces", self.you.faces, self.him.faces))
        print(tmp.format("Life", self.you.life, self.him.life))

