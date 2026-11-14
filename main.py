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
# Creation Date : 2020-04-21 - 15:51:46
"""
-----------
DOCSTRING

-----------
"""

import curses
import maps
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    box = curses.newwin(20, width-2, 1, 1)
    box.box()

    curses.curs_set(0)

    for i in range(len(maps.sword)):
        pic = maps.sword[i].split('\n')
        for j in range(len(pic)):
            box.addstr(3+j, 3, pic[j])
        box.refresh()
        time.sleep(0.2)
    box.refresh()

    key = -1
    while key not in [27, 113]:
        box.border(0)
        box.refresh()
        key = stdscr.getch()

        if key == 63: # h
            box.addstr(7, 3, 'Help')
            box.border(0)
            box.refresh()

curses.wrapper(main)
