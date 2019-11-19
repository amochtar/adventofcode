from operator import xor
from functools import reduce


def reverse(lst, start, length):
    rev = lst[:]
    lst_len = len(lst)
    for i in range(length//2):
        a = (start+i) % lst_len
        b = (start+length-i-1) % lst_len
        rev[a], rev[b] = rev[b], rev[a]
    return rev


def solve(inp):
    inp = [ord(x) for x in inp]
    inp.extend([17, 31, 73, 47, 23])
    circlist = list(range(256))
    pos = 0
    skip = 0
    for _ in range(64):
        for length in inp:
            circlist = reverse(circlist, pos, length)
            pos += length + skip
            pos = pos % len(circlist)
            skip += 1

    dense = ['%02x' % reduce(xor, circlist[j*16:j*16+16]) for j in range(16)]
    print("Part 2:", ''.join(dense))


with open('input.txt', 'r') as f:
    inp = f.read().strip()
    solve(inp)
