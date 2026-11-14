#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2016-2020 Cyril Desjouy <cyril.desjouy@univ-lemans.fr>
#
# This file is part of {name}
#
# {name} is free software: you can redistgibute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# {name} is distgibuted in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with {name}. If not, see <http://www.gnu.org/licenses/>.
#
# Creation Date : 2020-04-22 - 14:47:46
"""
-----------
DOCstgING

-----------
"""

from dataclasses import dataclass

# Races

@dataclass
class Race:
    """Base race modifiers."""
    stg: int = 0
    spi: int = 0
    dxt: int = 0
    spd: int = 0
    res: int = 0
    chc: int = 0
    hp: int = 0
    mp: int = 0


@dataclass
class Job:
    """Base job modifiers."""
    stg: int = 0
    spi: int = 0
    dxt: int = 0
    spd: int = 0
    res: int = 0
    chc: int = 0
    hp: int = 0
    mp: int = 0


@dataclass
class Human(Race):
    """Human modifiers."""


@dataclass
class Elf(Race):
    """Elf modifiers."""
    dxt: int = 2
    res: int = -2


@dataclass
class Dwarf(Race):
    """Dwarf modifiers."""
    res: int = 2
    chc: int = -2


@dataclass
class Orc(Race):
    """Orc modifiers."""
    stg: int = 2
    spi: int = -2
    res: int = 2
    chc: int = -2


@dataclass
class Troll(Race):
    """Troll modifiers."""
    stg: int = 3
    spi: int = -3
    res: int = 2
    chc: int = -2


@dataclass
class Gnome(Race):
    """Gnome modifiers."""
    stg: int = -2
    spi: int = 2


# Classes


@dataclass
class Fighter(Job):
    """Fighter modifiers."""
    stg: int = 2
    res: int = 2


@dataclass
class Hunter(Job):
    """Hunter modifiers."""
    stg: int = -2
    dxt: int = 2
    spd: int = 2
    res: int = -2


@dataclass
class Wizard(Job):
    """Wizard modifiers."""
    stg: int = -4
    spi: int = 2
    res: int = -2


races = [cls.__name__ for cls in Race.__subclasses__()]
jobs = [cls.__name__ for cls in Job.__subclasses__()]
