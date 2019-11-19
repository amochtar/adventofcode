import re
from collections import defaultdict

patt = re.compile(r'([xy])=(\d+), ([xy])=(\d+)..(\d+)')


def print_grid(grid):
    max_y = max(k[0] for k,v in grid.items() if v in '#') + 2
    min_x = min(k[1] for k,v in grid.items() if v!='.')
    max_x = max(k[1] for k,v in grid.items() if v!='.') + 2

    for y in range(max_y):
        for x in range(min_x, max_x):
            print(grid[(y,x)], end='')
        print()
    print()

def solve(input):
    grid = defaultdict(lambda: '.')
    start = (0,500)
    for line in input:
        m = re.match(patt, line)
        first, f, _, s1, s2 = m.groups()
        if first == 'x':
            x = int(f)
            for y in range(int(s1), int(s2)+1):
                grid[(y,x)] = '#'
        if first == 'y':
            y = int(f)
            for x in range(int(s1), int(s2)+1):
                grid[(y,x)] = '#'

    min_y = min(g[0] for g in grid.keys())
    max_y = max(g[0] for g in grid.keys())

    grid[start] = '+'
    drops = set([start])
    floods = set()
    while drops or floods:
        while drops:
            d = drops.pop()
            if d[0] > max_y:
                break

            if grid[d] == '+':
                drops.add((d[0]+1, d[1]))
                break
            elif grid[d] == '.':
                grid[d] = '|'
                drops.add((d[0]+1, d[1]))
            if grid[d] in '~#':
                floods.add((d[0]-1,d[1]))

        while floods:
            f = floods.pop()

            if grid[f] == '~':
                floods.add((f[0]-1, f[1]))
                continue

            open_left = False
            to_left = f[1]
            l = f
            while True:
                if grid[l] == '#':
                    to_left = l[1]+1
                    break
                if grid[l] in '.|' and grid[(l[0]+1, l[1])] in '.|':
                    to_left = l[1]
                    open_left = True
                    break
                l = (l[0],l[1]-1)

            open_right = False
            to_right = f[1]
            r = f
            while True:
                if grid[r] == '#':
                    to_right = r[1]-1
                    break
                if grid[r] in '.|' and grid[(r[0]+1, r[1])] in '.|':
                    to_right = r[1]
                    open_right = True
                    break
                r = (r[0],r[1]+1)

            if open_left or open_right:
                if open_left:
                    drops.add((f[0]+1,to_left))
                if open_right:
                    drops.add((f[0]+1,to_right))
                for i in range(to_left, to_right+1):
                    grid[(f[0], i)] = '|'
            else:
                floods.add((f[0]-1, f[1]))
                for i in range(to_left, to_right+1):
                    grid[(f[0], i)] = '~'

    print_grid(grid)
    print(len([v for k,v in grid.items() if v in '~|' and k[0]>=min_y and k[0]<=max_y]))
    print(len([v for k,v in grid.items() if v in '~' and k[0]>=min_y and k[0]<=max_y]))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
