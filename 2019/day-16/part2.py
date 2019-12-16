#!/usr/bin/env pypy3


def solve(input):
    input = input * 10000
    offset = int(''.join(map(str, input[:7])))

    # when the offset is in the second half of the input
    # the values become the cumulative sum of the this
    # and all following values
    assert len(input) // 2 < offset < len(input)

    # only need to consider values starting at offset
    # and reverse the list to make cumulative sum easier
    input = input[offset:][::-1]
    for i in range(100):
        cum = 0
        for j in range(len(input)):
            cum += input[j]
            input[j] = cum % 10

    print(''.join(map(str, input[::-1][:8])))


# with open('test.txt', 'r') as f:
#     input = [int(i) for i in f.read().strip()]
#     solve(input)

with open('input.txt', 'r') as f:
    input = [int(i) for i in f.read().strip()]
    solve(input)
