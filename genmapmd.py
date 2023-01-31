#!/usr/bin/env python3
from verify import solution_to_levels
sols = [
    '100110010101010001001100101110110101010010010011',
    '100110010101010010001100101110110101010010010011',
    '101010010101010001001100101110110101010100010110',
    '101010010101010010001100101110110101010100010110',
    '101100010101010001001100101110110101010100010110',
    '101100010101010010001100101110110101010100010110'
]
for solno, sol in enumerate(sols):
    levs = list(solution_to_levels(sol))
    with open(f'mapgen/route{solno+1}.md', 'w') as f:
        print('Start on level 1.\n', file=f)
        print('![level 1](out/001.png)\n', file=f)
        for a, b in zip(levs, levs[1:]):
            if b-a == 10:
                print(f'Collect all rings. Proceed to level {b}.\n', file=f)
            else:
                print(f'Don\'t collect all rings. Proceed to level {b}.\n', file=f)
            print(f'![level {b}](out/{b:03d}.png)\n', file=f)
        print('You\'re done!', file=f)
