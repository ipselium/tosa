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
# Creation Date : 2020-04-25 - 18:51:07
"""
-----------

All the exception used in the game.

-----------
"""


class BadOrientation(Exception):
    """Raise when providing a bad orientation."""


class NoBag(Exception):
    '''Raise this error if trying to acces a bag that does not exist.'''


class TooManyItems(Exception):
    '''Raise this exception when bag or deposit box is full.'''


class NoSuchAbility(Exception):
    """Raise this exception when calling an ability that does not exists or
    that is not available.
    """


class AlreadyDead(Exception):
    """Raise this exception when one of the involved characters is dead."""


class NoMana(Exception):
    """Raises this exception when there is not enough magic left to cast a spell."""
