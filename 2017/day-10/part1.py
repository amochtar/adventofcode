def reverse(lst, start, length):
    rev = lst[:]
    lst_len = len(lst)
    for i in range(length//2):
        a = (start+i) % lst_len
        b = (start+length-i-1) % lst_len
        rev[a], rev[b] = rev[b], rev[a]
    return rev


def solve(inp):
    inp = [int(x) for x in inp.split(',')]
    circlist = list(range(256))
    pos = 0
    skip = 0
    for length in inp:
        circlist = reverse(circlist, pos, length)
        pos += length + skip
        pos = pos % len(circlist)
        skip += 1

    print("Part 1:", circlist[0]*circlist[1])


with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
