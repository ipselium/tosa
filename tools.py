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
# Creation Date : 2020-04-28 - 20:27:07
"""
-----------
DOCSTRING

-----------
"""

import random


def chance(p1, p2, percent=50):
    """Determine whether a chance test is True of False."""
    val = p1.chc/p2.chc
    chc = random.random()
    if val >= 1:
        percent = percent/100 + (1 - 1/val)/2
        return True if chc <=  percent else False

    percent = max(0.01, percent/100 + (val - 1)/2)
    return True if chc <=  percent else False
