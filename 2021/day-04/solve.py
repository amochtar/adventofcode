#!/usr/bin/env python

import aoc


def parse_board(str):
    return [aoc.ints(line) for line in str.splitlines()]


def has_bingo(board, draws):
    for i in range(5):
        if all(n in draws for n in board[i]):
            return True
        if all(n in draws for n in list(zip(*board))[i]):
            return True
    return False


def score(board, draws):
    return draws[-1] * sum(n for line in board for n in line if n not in draws)


def draw(all_draws):
    for i in range(len(all_draws)):
        yield all_draws[:i+1]


@aoc.timing
def part1(boards, all_draws):
    for draws in draw(all_draws):
        for board in boards:
            if has_bingo(board, draws):
                return score(board, draws)
    return 0


@aoc.timing
def part2(boards, all_draws):
    for draws in draw(all_draws):
        new_boards = []
        for board in boards:
            if not has_bingo(board, draws):
                new_boards.append(board)

        if len(new_boards) == 0:
            return score(board, draws)
        boards = new_boards
    return 0


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     d, b = inp.split("\n\n", 1)
#     draws = aoc.ints(d)
#     boards = [parse_board(board) for board in b.split("\n\n")]

#     print("Part 1:", part1(boards, draws))
#     print("Part 2:", part2(boards, draws))

with open('input.txt', 'r') as f:
    inp = f.read()
    d, b = inp.split("\n\n", 1)
    draws = aoc.ints(d)
    boards = [parse_board(board) for board in b.split("\n\n")]

    print("Part 1:", part1(boards, draws))
    print("Part 2:", part2(boards, draws))
