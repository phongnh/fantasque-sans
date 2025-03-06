#!/usr/bin/env python3
# Adapted from https://github.com/larsenwork/monoid
# Copyright (c) 2015, Andreas Larsen and contributors.
# vim: sts=4 sw=4 ts=4 et

import sys
if len(sys.argv) < 5:
    usage = """Build should be run with 4 arguments:

    First: The total possible number of parallel processes (1+)
    Second: The parallel batch number (0+)
    Third: The .sfdir for the font
    Fourth: The output directory
    """
    print >> sys.stderr, usage
    exit(1)

from fontbuilder import *

# Output directory
output = sys.argv[4]

# # Options to generate
# conflicting(
#     style('Loose', Bearing(right=128)),
#     style('HalfLoose', Bearing(right=64)),
# #   style('normal', Bearing(left=0)),
#     style('HalfTight', Bearing(left=-64)),
#     style('Tight', Bearing(left=-128))
# )

conflicting(
#     option('XtraSmall', '13px', Line(x, x)),
#     option('Small', '14px', Line(x, x)),
# #   option('medium', 15px', Line(1650, 398)),
# #   option('LargeLineHeight', 'Large Line Height', Line(1750, 498)),
#     option('XtraLarge', '17px', Line(x, x))
    # option('Medium', 'Medium', Line(1850, 598)),
    # option('Medium', 'Medium', Line(1875, 623)),
    # option('Medium', 'Medium', Line(1975, 723)),
    # option('Large', 'Large', Line(2000, 748)),
    option('Large', 'Large', Line(2025, 773)),
    # option('ComicMono', 'ComicMono', [Line(2050, 798), SwapLookup('ss01')]),
    # option('XLarge', 'XLarge', Line(2125, 873))
    # option('XtraLarge', 'Xtra Large', Line(2150, 898))
)

# ss01
# option('NoLoopK', 'No loop k', SwapLookup('ss01'))
# option('Dollar', 'Alt $', Swap("dollar", "dollar.empty"))
# # ss03
# option('0', 'Alt 0', Swap("zero", "zero.dot"))
# # ss05
# option('1', 'Alt 1', Swap("one", "one.base"))
# # ss08
# option('l', 'Alt l', Swap("l", "l.zstyle"))
# # ss14
# # option('Squeeze', 'Squeezed capitals with diacritics', SwapLookup("ss14"))
# # no calt
# option('NoCalt', 'Turn off contextual alternates', DropCAltAndLiga())

# Build options in
build_batch(output, sys.argv[3], int(sys.argv[1]), int(sys.argv[2]))
