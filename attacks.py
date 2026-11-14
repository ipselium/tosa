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
# Creation Date : 2020-04-25 - 18:54:24
"""
-----------

All about magic.

-----------
"""

from exceptions import NoSuchAbility


class Attacks:
    """Create Attacks instances."""

    def __init__(self, job):
        self._upgrade_tree = {'close': ('normal', 'rage', 'fury'),
                              'distant': ('single', 'multi')}

        self.lst = ['normal']
        if job == 'Fighter':
            self.lst.append('rage')
        elif job == 'Hunter':
            self.lst.append('single')

    def __call__(self, p1, p2, subtype):
        if subtype in self.lst:
            return getattr(self, subtype)(p1, p2)

        raise NoSuchAbility('No such attack')

    @staticmethod
    def normal(p1, p2):
        """Normal attack"""
        value = max(1, p1.atk_strength - (p2.stats.res + p2.stats.res_mod))
        p2.stats.hp = max(0, p2.stats.hp - value)
        p2.stats.res_mod -= min(p2.stats.res_mod + p2.stats.res, value)
        return value


class Invocations:
    """Create invocation instances."""

    def __init__(self):
        self._lst_complete = ['fire', 'ice', 'earth', 'water']
        self.lst = []

    def fire(self):
        """Return a Fire elemental"""

    def ice(self):
        """Return a Ice elemental"""

    def earth(self):
        """Return a Earth elemental"""

    def water(self):
        """Return a Water elemental"""


class Spells:
    """Spells instances"""

    def __init__(self, job):
        self._upgrade_tree = {'fire': ('fire1', 'fire2', 'fire3'),
                              'ice': ('ice1', 'ice2', 'ice3'),
                              'silence': ('silence1', 'silence2'),
                              'shield': ('shield1', 'shield2'),
                              'heal': ('heal1', 'heal2', 'heal3'),
                              'sleep': ('sleep1', 'sleep2'),}
        if job == 'Wizard':
            self.lst = ['fire1', 'heal1', 'shield1']
        else:
            self.lst = []


    def __call__(self, p1, p2, subtype):
        if subtype in self.lst:
            return getattr(self, subtype)(p1, p2)
        raise NoSuchAbility('No such spell')

    @staticmethod
    def fire1(p1, p2):
        """Fire Level 1 : Fireball"""
        value = max(1, p1.spl_strength - (p2.stats.res + p2.stats.res_mod))
        p2.stats.hp = max(0, p2.stats.hp - value)
        p2.stats.res_mod -= min(p2.stats.res_mod + p2.stats.res, value)
        p1.stats.mp = max(0, p1.stats.mp - 1)
        return value

    @staticmethod
    def fire2(p1, p2):
        """Fire Level 2 : """

    @staticmethod
    def fire3(p1, p2):
        """Fire Level 3 : Fire rain"""
