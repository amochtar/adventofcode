#!/usr/bin/env python

from typing import List
import aoc
import regex as re


def rule_parts(rule):
    return [r.split(' ') for r in rule.split(' | ')]


def to_regex(rules, r, used=[]) -> str:
    rule = rules[r]
    rx = []
    for sub_rules in rule:
        sub_rule_rx = ""
        for sub_rule in sub_rules:
            if sub_rule.startswith('"'):
                sub_rule_rx += sub_rule.strip('"')
            elif r in used:
                # recursive rule
                sub_rule_rx += f'(?&r{r})?'
            else:
                sub_rule_rx += to_regex(rules, sub_rule, used + [r])
        rx.append(sub_rule_rx)

    return f'(?<r{r}>{"|".join(rx)})'


def solve(inp: str):
    rules, messages = inp.split('\n\n')
    rules = {rule.split(': ')[0]: rule_parts(rule.split(': ')[1])
             for rule in rules.splitlines()}

    rx = to_regex(rules, '0')
    rule_rx = re.compile(rx)
    print("Part 1:", sum(rule_rx.fullmatch(m) !=
                         None for m in messages.splitlines()))

    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    rx = to_regex(rules, '0')
    rule_rx = re.compile(rx)
    print("Part 2:", sum(rule_rx.fullmatch(m) !=
                         None for m in messages.splitlines()))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
