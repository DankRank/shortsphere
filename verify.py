#!/usr/bin/env python3
import sys

# cross-checking with this implementation
# https://web.archive.org/web/20200805205421id_/http://www.din.or.jp/~koryan/sonic/gbs-anlz.js
def levtopmn(lev):
    pmn = [0]*4
    pmn[0] = (lev - 1) % 128
    pmn[1] = (1 + ((lev - 1) % 127) * 3) % 127
    pmn[2] = (2 + ((lev - 1) % 126) * 5) % 126
    pmn[3] = (3 + ((lev - 1) % 125) * 7) % 125
    return pmn

def solution_to_levels(sol):
    lev = 1
    yield lev
    for x in sol:
        assert x in '01'
        lev += 10 if x == '1' else 1
        yield lev

visited = set()
for lev in solution_to_levels(sys.argv[1]):
    visited.update(levtopmn(lev))
print(visited == set(range(128)))
