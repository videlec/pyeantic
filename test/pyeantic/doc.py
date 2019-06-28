#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
#  This file is part of pyeantic.
#
#        Copyright (C) 2019 Vincent Delecroix
#        Copyright (C) 2019 Julian Rüth
#
#  pyeantic is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or (at your
#  option) any later version.
#
#  pyeantic is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with pyeantic. If not, see <https://www.gnu.org/licenses/>.
#####################################################################

import sys
import pytest
import doctest


if __name__ == '__main__':
    try:
        import sage.all
    except InportError:
        sys.exit(0)
    import pyeantic.sage_conversion
    sys.exit(doctest.testmod(pyeantic.sage_conversion).failed)

