# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis/
#
# Most of this work is copyright (C) 2013-2020 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.
#
# END HEADER

from hypothesis.internal.conjecture.dfa import ConcreteDFA

SHRINKING_DFAS = {}

# Note: Everything below the following line is auto generated.
# Any code added after this point will be deleted by an automated
# process. Don't write code below this point.
#
# AUTOGENERATED BEGINS

# fmt: off

SHRINKING_DFAS['datetimes()-1478f1f696'] = ConcreteDFA([[(0, 1), (1, 255, 2)], [(0, 3), (1, 255, 4)], [(0, 255, 4)], [(0, 5), (1, 255, 6)], [(0, 255, 6)], [(4, 255, 7)], [(0, 255, 8)], [(1, 9)], [(0, 1, 9)], []], {9})  # noqa: E501
SHRINKING_DFAS['emails()-fde8f71142'] = ConcreteDFA([[(0, 1), (1, 255, 2)], [(0, 255, 2)], []], {2})  # noqa: E501
SHRINKING_DFAS['floats()-58ab5aefc9'] = ConcreteDFA([[(1, 1), (2, 255, 2)], [(1, 3)], [(0, 1, 3)], []], {3})  # noqa: E501
SHRINKING_DFAS['floats()-6b86629f89'] = ConcreteDFA([[(3, 1), (4, 255, 2)], [(1, 3)], [(0, 1, 3)], []], {3})  # noqa: E501
SHRINKING_DFAS['floats()-aa8aef1e72'] = ConcreteDFA([[(2, 1), (3, 255, 2)], [(1, 3)], [(0, 1, 3)], []], {3})  # noqa: E501
SHRINKING_DFAS['floats()-bf71ffe70f'] = ConcreteDFA([[(4, 1), (5, 255, 2)], [(1, 3)], [(0, 1, 3)], []], {3})  # noqa: E501
SHRINKING_DFAS['non_integer_floats()-2fdf36bca8'] = ConcreteDFA([[(128, 191, 1), (192, 255, 2)], [(0, 3), (1, 127, 4), (128, 255, 3)], [(0, 255, 4)], [(0, 5), (1, 255, 6)], [(0, 255, 6)], [(0, 7), (1, 255, 8)], [(0, 255, 8)], [(0, 9), (1, 255, 10)], [(0, 255, 10)], [(0, 11), (1, 255, 12)], [(0, 255, 12)], [(0, 13), (1, 255, 14)], [(0, 255, 14)], [(1, 255, 15)], [(0, 255, 15)], []], {15})  # noqa: E501
SHRINKING_DFAS['text()-05c917b389'] = ConcreteDFA([[(0, 1), (1, 8, 2)], [(9, 255, 3)], [(0, 255, 4)], [], [(0, 255, 5)], [(0, 255, 3)]], {3})  # noqa: E501
SHRINKING_DFAS['text()-807e5f9650'] = ConcreteDFA([[(0, 8, 1), (9, 255, 2)], [(1, 8, 3)], [(1, 8, 3)], [(0, 4)], [(0, 255, 5)], []], {2, 5})  # noqa: E501

# fmt: on
