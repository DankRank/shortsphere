#!/usr/bin/env python3
from verify import levtopmn, solution_to_levels
sols = [
    '100110010101010001001100101110110101010010010011', # red
    '100110010101010010001100101110110101010010010011', # red
    '101010010101010001001100101110110101010100010110', # blue
    '101010010101010010001100101110110101010100010110', # blue
    '101100010101010001001100101110110101010100010110', # blue
    '101100010101010010001100101110110101010100010110'  # blue
]
nodes = set()
edges = set()
for sol in sols:
    levs = list(solution_to_levels(sol))
    nodes.update(levs)
    edges.update(zip(levs, levs[1:]))
print('digraph { nodesep=0.1; ranksep=0.1;')
for a in sorted(nodes):
    print(f'{a} [width=.5;height=.2;margin=0;fontsize=12;xlabel=<<FONT POINT-SIZE="10">{tuple(levtopmn(a))}</FONT>>]')
for a, b in sorted(edges):
    s = ''
    if b-a == 10:
        s = '[arrowhead=odot]'
    if a in (12, 211, 235):
        if b-a == 10:
            s += '[color=blue]'
        else:
            s += '[color=red]'
    print(f'{a} -> {b} {s}')
print('}')
