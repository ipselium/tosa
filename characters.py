#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2016-2020 Cyril Desjouy <cyril.desjouy@univ-lemans.fr>
#
# This file is part of {name}
#
# {name} is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# {name} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with {name}. If not, see <http://www.gnu.org/licenses/>.
#
# Creation Date : 2020-04-23 - 16:46:44
"""
-----------

All about game characters

-----------
"""


import random
import math
from exceptions import AlreadyDead, NoMana, NoBag, TooManyItems
import modifiers
import items
from attacks import Attacks, Spells
from tools import chance


class BaseStats:
    """Create basic statistics of a character."""

    def __init__(self, race, job, level=1):

        self.race = race
        self.job = job
        self.level = level

        self._xp = 0
        self._base_stat = 10
        self._base_bonus = [-2] + 2*[-1] + [0, 0] + 2*[1] + 1*[2]
        self.res_mod = 0
        self._init_race_stats()
        self._init_job_stats()
        self._init_level_stats(self.level)

    def _init_race_stats(self):

        race = getattr(modifiers, self.race)()

        self.stg = self._base_stat + race.stg
        self.spi = self._base_stat + race.spi
        self.dxt = self._base_stat + race.dxt
        self.spd = self._base_stat + race.spd
        self.res = self._base_stat + race.res
        self.chc = self._base_stat + race.chc
        self.hp = self._base_stat + race.hp
        self.mp = self._base_stat + race.mp

    def _init_job_stats(self):

        job = getattr(modifiers, self.job)()

        self.stg += job.stg + self._bonus
        self.spi += job.spi + self._bonus
        self.dxt += job.dxt + self._bonus
        self.spd += job.spd + self._bonus
        self.res += job.res + self._bonus
        self.chc += job.chc + self._bonus
        self.hp += job.hp + self._bonus
        self.mp += job.mp + self._bonus

    def _init_level_stats(self, level):

        mod = getattr(modifiers, self.job)()

        for _ in range(level):
            self.stg += self._evolution(mod.stg)
            self.spi += self._evolution(mod.spi)
            self.dxt += self._evolution(mod.dxt)
            self.spd += self._evolution(mod.spd)
            self.res += self._evolution(mod.res)
            self.chc += self._evolution(mod.chc)
            self.hp += self._evolution(mod.hp)
            self.mp += self._evolution(mod.mp)

    @property
    def _base_stat_list(self):
        stats = []
        stats.append(f'stg: {self.stg}')
        stats.append(f'res: {self.res} [{self.res_mod}]')
        stats.append(f'dxt: {self.dxt}')
        stats.append(f'spd: {self.spd}')
        stats.append(f'spi: {self.spi}')
        stats.append(f'chc: {self.chc}')
        stats.append(f'hp: {self.hp}')
        stats.append(f'mp: {self.mp}')
        stats.append(f'tot: {self._total}')
        return stats

    @staticmethod
    def _evolution(arg):
        return int(5 + arg)

    def upgrade_repartition(self):
        """Show repartition of upgrades following modifiers."""
        for mod in range(-4, 5):
            print(f"Mod : {mod:+} => {self._evolution(mod)}")

    @property
    def _bonus(self):
        return self._base_bonus.pop(random.randrange(len(self._base_bonus)))

    @property
    def _total(self):
        return self.stg + self.spi + self.dxt + self.spd + self.res + \
                self.chc + self.hp + self.mp

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        self._xp = value
        if self._xp > 100:
            self._upgrade()

    def _upgrade(self):
        self.level += 1
        self.xp -= 100
        print('Upgrade')
        self._init_level_stats(1)


class Character:
    '''Base class for characters.'''

    def __init__(self, name, race, job, level=1, bag=None, weapon=None, suit=None, bot=False):

        self.name = name
        self.race = race
        self.job = job
        self.stats = BaseStats(race, job, level=level)

        self.bag = bag
        self.weapon = weapon if weapon else items.BareHands()
        self.suit = suit if suit else items.Suit(job)

        self.spl_tree = Spells(self.job)
        self.atk_tree = Attacks(self.job)
        self.alive = True
        self.bot = bot
        self.location = [1, 0, 0]
        self._msg_atk = '{0} hits {1} with an {2}-strength.\n'
        self._msg_atk += '{1} has now {3} life and lose {4} resistance points.'
        self._msg_spl = '{0} hits {1} with an {2}-strength.\n'
        self._msg_spl += '{1} has now {3} life and lose {4} resistance points.'

        self.stdout = self._stdout
        self.stdin = self._stdin

    def action(self):
        """Combat actions."""

        if self.bot:
            self._ai_action()
        else:
            self._pl_action()

    def _ai_action(self):
        print(f'{self.name} action [ai]')
        self.alive = False

    def _pl_action(self):
        print(f'{self.name} action [pl]')

    def attack(self, other, subtype):
        """Attack another character"""
        self._check_dead(other)
        self.stdout(f'{self.name} is attacking {other.name}')
        if self.weapon.attr in ['1-hand', '2-hand', 'melee']:
            reaction = other._ai_under_melee_attack(self)
        elif self.weapon.attr == 'ranged':
            reaction = other._ai_under_ranged_attack(self)

        if reaction:
            value = self.atk_tree(self, other, subtype)*reaction
            self.stdout(self._msg_atk.format(self.name, other.name, value,
                                             other.stats.hp, abs(other.stats.res_mod)))
        self._check_killed(other)

    def spell(self, other, subtype):
        """Cast a spell."""
        self._check_dead(other)
        self.stdout(f'{self.name} is casting {subtype} on {other.name}')
        reaction = other._ai_under_ranged_attack(self)

        if reaction:
            if self.stats.mp:
                value = self.spl_tree(self, other, subtype)*reaction
                self.stdout(self._msg_spl.format(self.name, other.name, value,
                                                 other.stats.hp, abs(other.stats.res_mod)))
                self._check_killed(other)
            else:
                raise NoMana('No more mana...')

    def block(self, other):
        """Block an attack"""
        if self._check_block(other):
            self.stdout(f'{self.name} blocked {other.name} attack')
            if self._check_counter(other):
                self.attack(other, 'normal')
            return 0

        self.stdout(f'{self.name} tried to block {other.name} attack but failed')
        return 2

    def dodge(self, other):
        """Dodge an attack"""
        if self._check_dodge(other):
            self.stdout(f'{self.name} dodged {other.name} attack')
            return 0

        self.stdout(f'{self.name} tried to dodge {other.name} attack, but failed')
        return 3

    def escape(self, other):
        """Escape combat."""
        if chance(self, other, self.spd/other.spd*100):
            self.stdout(f'{self.name} escaped combat.')
            return True
        self.stdout(f'{self.name} failed to escape combat.')
        return False

    def steal(self, other):
        """Steal an item."""
        if not self.bag:
            raise NoBag(f'{self.name} has no bag')

        if not other.bag:
            raise NoBag(f'{other.name} has no bag')

        if chance(self, other, self.dxt/other.dxt*100) and other.bag.content:
            item = random.choice(other.bag.content)
            try:
                self.bag.add(item)
            except TooManyItems:
                self.stdout(f'{self.name} tried to steal {other.name} but bag is full')
            else:
                other.bag.content.remove(item)
                self.stdout(f'{self.name} stole a {item.name}')

    def move(self, direction):
        """Move."""
        if direction not in ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']:
            raise BadOrientation('Bad orientation.')
        if 'e' in direction:
            self.location[1] -= 1
        if 'w' in direction:
            self.location[1] += 1
        if 's' in direction:
            self.location[2] -= 1
        if 'n' in direction:
            self.location[2] += 1

    def _ai_under_melee_attack(self, other):
        """Reaction of a contested AI."""
        if 0 < random.random() < 0.2:
            return self.block(other)

        if 0.2 <= random.random() > 0.4:
            return self.dodge(other)

        return 1

    def _ai_under_ranged_attack(self, other):
        """Reaction of a contested AI."""
        if 0 <= random.random() > 0.2:
            return self.dodge(other)
        return 1

    def _under_attack(self, other):
        """Implement a timer => Answer time linked to """

    @staticmethod
    def _stdout(msg):
        """Print message to stdout"""
        print(msg)

    @staticmethod
    def _stdin(msg):
        """Ask user for input."""
        return input(msg)

    @property
    def atk_strength(self):
        """Return attack value."""
        return self.stg + self.weapon.atk_mod

    @property
    def spl_strength(self):
        """Return spell value."""
        return self.spi + self.weapon.atk_mod

    @property
    def stg(self):
        """Returns base strength value + all modifiers."""
        return self.stats.stg + self.weapon.stg_mod + self.suit.stg_mod

    @property
    def spi(self):
        """Returns base spirit value + all modifiers."""
        return self.stats.spi + self.weapon.spi_mod + self.suit.spi_mod

    @property
    def dxt(self):
        """Returns base dexterity value + all modifiers."""
        return self.stats.dxt + self.weapon.dxt_mod + self.suit.dxt_mod

    @property
    def spd(self):
        """Returns base speed value + all modifiers."""
        return self.stats.spd + self.weapon.spd_mod + self.suit.spd_mod

    @property
    def res(self):
        """Returns base resistance value + all modifiers."""
        return self.stats.res + self.weapon.res_mod + self.suit.res_mod

    @property
    def chc(self):
        """Returns base chance value + all modifiers."""
        return self.stats.chc + self.weapon.chc_mod + self.suit.chc_mod

    def _check_dead(self, other):
        if not other.alive:
            raise AlreadyDead(f'{other.name} is dead')
        if not self.alive:
            raise AlreadyDead(f'{self.name} is dead')

    def _check_killed(self, other):
        if not other.stats.hp:
            other.alive = False
            value = max(10, (other.stats.level - self.stats.level)*10)
            value += random.randint(0, int(value/4))
            self.stats.xp += value
            self.stdout(f'{self.name} gained {value} xp.')

    def _check_counter(self, other):
        """Counter an attack."""
        smin = 0.10*math.sqrt(self.stats.level/other.stats.level)
        scom = 2 - other.stats.dxt/self.stats.dxt - other.stats.spd/self.stats.spd
        if max(smin, scom) > random.random():
            return True
        return False

    def _check_block(self, other):
        """Block an attack."""
        s = (self.stats.dxt + self.stats.stg) - (other.stats.dxt + other.stats.stg) > 0
        c = (1 - other.stats.chc/self.stats.chc) > random.random()
        if s and c:
            return True
        return False

    def _check_dodge(self, other):
        """Dodge an attack."""
        return self._check_counter(other)

    def __str__(self):
        stats = [f'{self.name} [{self.stats.race} {self.stats.job} Lvl. {self.stats.level}]']
        s = self.stats._base_stat_list
        for i, j in zip(s[::2], s[1::2]):
            stats += [f'\t{i:<16}\t{j:<16}']
        stats += [f'Weapon: {self.weapon.name}']
        stats += [f'Bag: {self.bag}'] if self.bag else ['No Bag']
        return '\n'.join(stats)


def get_random_char(loc, lvl, bot=True):
    """Return random character."""
    race = random.choice(modifiers.races)
    job = random.choice(modifiers.jobs)

    bag, = random.choices((None, items.Bag(fill_lvl=lvl)), (80, 20))
    weapon, = random.choices([None, items.get_random_item(lvl=lvl, kind='weapon', job=job)],
                             [40, 60])

    return Character(f'{loc} {race}', race, job, level=lvl, bag=bag, weapon=weapon, bot=bot)
