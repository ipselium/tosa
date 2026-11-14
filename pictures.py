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
# Creation Date : 2020-04-29 - 16:35:16
"""
-----------
DOCSTRING

-----------
"""

window = """
  ___.oOo.___
 |           |
 |           |
 |           |
 |           |
 |           |
_|___________|_
^^^^^^^^^^^^^^^"""


walking = [
".oOOo.", ".OOOO.", "oOOOOo",
"OOOOOO", "OOooOO", "Oo..oO",
"o....o", "......", "o....o",
"..OO.."]

sword = [
"""
     />
[####[.]==============>
     \>
""",
"""
     />
[####[o]==============>
     \>
""",
"""
     />
[####[O]D=============>
     \>
""",
"""
     />
[####[o]==DB==========>
     \>
""",
"""
     />
[####[.]===DBBB=======>
     \>
""",
"""
     />
[####[o]====DBBBB=====>
     \>
""",
"""
     />
[####[O]=====DBBBBo===>
     \>
""",
"""
     />                 /-\\
[####[o]======DBBBBBBO> |O|
     \>                 \\_/
""",
"""
     />                   /-\\
[####[o]=======DBBBBBo>   |O|
     \>                   \\_/
""",
"""
     />                     /-\\
[####[o]========DBBBo.>     |O|
     \>                     \\_/
""",
"""
     />                       /-\\
[####[o]=========DBBo.>       |O|
     \>                       \\_/
""",
"""
     />                         /-\\
[####[o]============Do>         |O|
     \>                         \\_/
""",
"""
     />                           /-\\
[####[o]==============>           |O|
     \>                           \\_/
"""
]
