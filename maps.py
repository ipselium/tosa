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
# Creation Date : 2020-04-21 - 16:50:55
"""
-----------
 ~  : River/ocean
 ƒ  : Forest
^Ʌ^ : Moutains
... : Plains
 ~  : Swamp
+†+  : Cemetary
<O> : You
 ¤  : Cave
 Ʌ
^H^ : Village
-----------
"""

rmap ="""
   ^Ʌ^^Ʌ^                                      ,    ƒ  ,        __       _,~-~-
     ^Ʌ^                                      ,       ,        , _ `    , _,~-
    ^Ʌ^^Ʌ^                                   ,       ,        , , ` `  / /
   ^Ʌ^^Ʌ^                                   ,   ƒ   (        , ,   ` `- /
   ^Ʌ^¤                                    (         `      ' '     `__/
  ^Ʌ^^Ʌ^                                    `-        `     '~'        ^A^
    ^Ʌ^                                       `       '      ` `
     ^                                         `  ƒ  '        ' '           ^A^
                                                `   '         ,~,
                                                  `_'         , ,        +†+










+-------------+
| TERRA NUEVA |
+-------------+
"""


raw_map = """
  M                          FFFFFFFFFFFFFFFFFFFFFFFF                    WWW
  MM                         FFFFFFFFFFFFFFFFFFFFFFFFF                  WWW
  MMM                         FFFFFFFFFFFFFFFFFFFFFFFFF                WWW
  MM                           FFFFFFFFFFFFFFFFFFFFFFF                  WWW
   MM                           FFFFFFFFFFFFFFFFFFFFF                 WWW
    MM                           FFFFFF   FFFFFFFFFF                 WWW
   MMOM                           FFFF  O  FFFFFFFF   V             WWW VV
     MMM                            FFF   FFFFFFFF                 WWW VVVV
      MMM                            FFFFFFFFFFFFF                WWW  VV
       M                              FFFFFFFFFFF                  WWW
                                        FFFFFFF                   WWW
            V                             FFF                    WWW
                                                                WWW        V
                                                               WWW           C
                                                              WWW
"""






if __name__ == "__main__":
    print(rmap)
