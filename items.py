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
# Creation Date : 2020-04-23 - 16:35:08
"""
-----------
Items
-----------
"""

import re
import random
from dataclasses import dataclass
from exceptions import TooManyItems


# Inventory


class Bag:
    """Bag class."""

    def __init__(self, size=9, fill_lvl=None):
        self.size = size
        self.content = []
        if isinstance(fill_lvl, int):
            self.fill(fill_lvl)

    @property
    def _total_clutter(self):
        return sum([item.clutter for item in self.content])

    def add(self, obj):
        """Add an item (obj) to bag."""
        if self.size - (self._total_clutter + obj.clutter) >= 0:
            self.content.append(obj)
        else:
            raise TooManyItems('Too many items')

    def fill(self, lvl):
        """Randomly fill the bag with items/potions."""
        for _ in range(random.randint(0, 2)):
            self.add(Potion.of('random'))
        if random.random() > 0.7:
            self.add(get_random_item(lvl=lvl))

    def drop(self, idx):
        """Drop an item based on its index in self.content."""
        self.content.remove(idx)

    def __str__(self):
        items = f"Bag [{self._total_clutter}/{self.size}]\n"
        for idx, item in enumerate(self.content):
            items += f'\tslot {idx+1}: {item.name} [{item.clutter}]\n'
        return items


class DepositBox(Bag):
    """The deposit box."""


# Potions


class Potion:
    """Potion class."""

    clutter = 1
    types = {'BH': ('Basic Healing Potion', 'hp', 50),
             'GH': ('Great Healing Potion', 'hp', 75),
             'SH': ('Super Healing Potion', 'hp', 100),
             'BM': ('Basic Magic Potion', 'mp', 50),
             'GM': ('Great Magic Potion', 'mp', 75),
             'SM': ('Super Magic Potion', 'mp', 100),
             'BR': ('Basic Resistance Potion', 'res', 50),
             'GR': ('Great Resistance Potion', 'res', 75),
             'SR': ('Super Resistance Potion', 'res', 100),
             'BS': ('Basic Strength Potion', 'stg', 50),
             'GS': ('Great Strength Potion', 'stg', 75),
             'SS': ('Super Strength Potion', 'stg', 100)}

    def __init__(self, name, attribute, value=50):
        self.name = name
        self.attribute = attribute
        self.value = value

    @classmethod
    def of(cls, kind):
        """Create an instance of Potion among the templates defined in Potion.types."""
        if kind == 'random':
            kind = random.choice(list(cls.types.keys()))
        return Potion(*cls.types[kind])

    def __str__(self):
        return f"{self.name} (+{self.value} % {self.attribute})"


# Suit


class Suit:
    """Gather all pieces of equipement."""

    def __init__(self, job):
        self._head = Nothing()
        self._arms = Nothing()
        self._hands = Nothing()

        if job in ['wizard']:
            self._chest = Robe()
            self._legs = Nothing()
            self._feet = LeatherBoots()
        elif job in ['hunter', 'fighter']:
            self._chest = LeatherArmor()
            self._legs = LeatherPants()
            self._feet = LeatherBoots()
        else:
            self._chest = LeatherArmor()
            self._legs = LeatherPants()
            self._feet = LeatherBoots()

    @property
    def head(self):
        """Headwear."""
        return self._head

    @property
    def arms(self):
        """Armswear."""
        return self._arms

    @property
    def hands(self):
        """Handswear."""
        return self._hands

    @property
    def legs(self):
        """Legswear"""
        return self._legs

    @property
    def feet(self):
        """Feetwear"""
        return self._feet

    @property
    def chest(self):
        """Chestwear"""
        return self._chest

    @property
    def suit(self):
        """Returns all suit elements."""
        return [self.head, self.arms, self.hands, self.legs, self.feet, self.chest]

    @property
    def stg_mod(self):
        """Strength modifier."""
        mod = 0
        for piece in self.suit:
            mod += piece.stg_mod
        return mod

    @property
    def res_mod(self):
        """Resistance modifier."""
        mod = 0
        for piece in self.suit:
            mod += piece.res_mod
        return mod

    @property
    def dxt_mod(self):
        """Dexterity modifier."""
        mod = 0
        for piece in self.suit:
            mod += piece.dxt_mod
        return mod

    @property
    def spd_mod(self):
        """Speed modifier."""
        mod = 0
        for piece in self.suit:
            mod += piece.spd_mod
        return mod

    @property
    def spi_mod(self):
        """Spirit modifier."""
        mod = 0
        for piece in self.suit:
            mod += piece.spi_mod
        return mod

    @property
    def chc_mod(self):
        """Chance modifier."""
        mod = 0
        for piece in self.suit:
            mod += piece.chc_mod
        return mod


# Items


@dataclass
class EquipmentPiece:
    """Template for equipement pieces."""
    kind: str = None
    attr: str = None
    level: int = 1
    rarity: str = None
    clutter: int = 0
    favorite: str = None

    atk_mod: int = 0
    blk_mod: int = 0

    stg_mod: int = 0
    res_mod: int = 0
    dxt_mod: int = 0
    spd_mod: int = 0
    spi_mod: int = 0
    chc_mod: int = 0

    def __post_init__(self):
        self.name = re.sub(r"(\w)([A-Z])", r"\1 \2", type(self).__name__)


@dataclass
class Nothing(EquipmentPiece):
    """Unarmed."""


# Simple Clothes

@dataclass
class ClothTunic(EquipmentPiece):
    """Cloth tunic."""
    kind: str = 'chest'
    clutter: int = 1
    rarity: str = 'c'
    res_mod: int = 1


@dataclass
class ClothPants(EquipmentPiece):
    """Leather pants."""
    kind: str = 'pants'
    clutter: int = 1
    rarity: str = 'c'
    res_mod: int = 1


@dataclass
class Shoes(EquipmentPiece):
    """Basic shoes."""
    kind: str = 'feet'
    clutter: int = 2
    rarity: str = 'c'
    res_mod: int = 1


# Leather clothes

@dataclass
class LeatherTunic(EquipmentPiece):
    """Leather tunic."""
    kind: str = 'chest'
    clutter: int = 1
    rarity: str = 'u'
    res_mod: int = 2


@dataclass
class LeatherArmor(EquipmentPiece):
    """Leather armor."""
    kind: str = 'chest'
    clutter: int = 2
    rarity: str = 'u'
    res_mod: int = 3
    dxt_mod: int = -1


@dataclass
class LeatherPants(EquipmentPiece):
    """Leather pants."""
    kind: str = 'pants'
    clutter: int = 2
    rarity: str = 'u'
    res_mod: int = 2


@dataclass
class LeatherGloves(EquipmentPiece):
    """Leather gloves."""
    kind: str = 'hands'
    clutter: int = 1
    rarity: str = 'u'
    res_mod: int = 2


@dataclass
class LeatherBoots(EquipmentPiece):
    """Leather boots."""
    kind: str = 'feet'
    clutter: int = 2
    rarity: str = 'u'
    res_mod: int = 2


# Common weapons


@dataclass
class BareHands(EquipmentPiece):
    """Unarmed."""
    name: str = 'Bare hands'
    kind: str = 'weapon'
    attr: str = 'melee'


@dataclass
class ShortSword(EquipmentPiece):
    """Short sword."""
    kind: str = 'weapon'
    attr: str = '1-hand'
    clutter: int = 2
    rarity: str = 'c'
    favorite: str = 'Fighter'

    atk_mod: int = 6
    blk_mod: int = 2


@dataclass
class ShortBow(EquipmentPiece):
    """Short bow."""
    kind: str = 'weapon'
    attr: str = 'ranged'
    clutter: int = 2
    rarity: str = 'c'
    favorite: str = 'Hunter'

    atk_mod: int = 8


@dataclass
class ShortStaff(EquipmentPiece):
    """Short staff."""
    kind: str = 'weapon'
    attr: str = '2-hand'
    clutter: int = 2
    rarity: str = 'c'
    favorite: str = 'Wizard'

    atk_mod: int = 1
    blk_mod: int = 1

    spi_mod: int = 6


# Uncommon weapons


@dataclass
class LongSword(EquipmentPiece):
    """Long sword."""
    kind: str = 'weapon'
    attr: str = '1-hand'
    clutter: int = 3
    rarity: str = 'u'
    favorite: str = 'Fighter'

    atk_mod: int = 9
    blk_mod: int = 1


@dataclass
class LongBow(EquipmentPiece):
    """Long bow."""
    kind: str = 'weapon'
    attr: str = 'ranged'
    clutter: int = 3
    rarity: str = 'u'
    favorite: str = 'Hunter'

    atk_mod: int = 10


@dataclass
class LongStaff(EquipmentPiece):
    """Long staff."""
    kind: str = 'weapon'
    attr: str = '2-hand'
    clutter: int = 3
    rarity: str = 'u'
    favorite: str = 'Wizard'

    atk_mod: int = 2
    blk_mod: int = 2

    spi_mod: int = 8



def get_items_by_rarity(kind=None, job=None):
    """Returns 4 lists of item classified by rarity:
        * Common items,
        * Uncommon items,
        * Rare items,
        * Mythic items.
    """

    c = [item for item in get_item_list() if item.rarity == 'c']
    u = [item for item in get_item_list() if item.rarity == 'u']
    r = [item for item in get_item_list() if item.rarity == 'r']
    m = [item for item in get_item_list() if item.rarity == 'm']

    if kind:
        c = [item for item in c if item.kind == kind]
        u = [item for item in u if item.kind == kind]
        r = [item for item in r if item.kind == kind]
        m = [item for item in m if item.kind == kind]
    if job:
        c = [item for item in c if item.favorite in (job, None)]
        u = [item for item in u if item.favorite in (job, None)]
        r = [item for item in r if item.favorite in (job, None)]
        m = [item for item in m if item.favorite in (job, None)]

    return {'c': c, 'u': u, 'r': r, 'm': m}


def get_item_list():
    """Get the list of all items."""
    return [cls for cls in EquipmentPiece.__subclasses__() if cls.rarity]


def get_random_item(lvl=1, kind=None, job=None):
    """Get random item as function of character level."""

    item_list = get_items_by_rarity(kind, job)

    if lvl < 5:
        rarity, = random.choices(('c', 'u'), (90, 10))
        return random.choice(item_list[rarity])()

    if lvl < 10:
        rarity, = random.choices(('c', 'u', 'r'), (80, 15, 5))
        return random.choice(item_list[rarity])()

    if lvl < 20:
        rarity, = random.choices(('c', 'u', 'r', 'm'), (70, 20, 9.5, 0.5))
        return random.choice(item_list[rarity])()

    if lvl < 30:
        rarity, = random.choices(('c', 'u', 'r', 'm'), (60, 25, 14, 1))
        return random.choice(item_list[rarity])()
    if lvl < 40:
        rarity, = random.choices(('c', 'u', 'r', 'm'), (50, 30, 18, 2))
        return random.choice(item_list[rarity])()

    if lvl < 50:
        rarity, = random.choices(('c', 'u', 'r', 'm'), (40, 35, 21, 4))
        return random.choice(item_list[rarity])()

    rarity, = random.choices(('c', 'u', 'r', 'm'), (30, 40, 25, 5))
    return random.choice(item_list[rarity])()
