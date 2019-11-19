import numpy as np
import re
from collections import Counter
from collections import defaultdict
from operator import itemgetter

f = open("input.txt", "r")
input = f.readlines()
strings = [x.strip() for x in input]


def str_value(s):
    length = 0
    s = s[1:-1]
    i = 0
    while i < len(s):
        if s.startswith('\\x', i):
            i += 4
        elif s[i] == '\\':
            i += 2
        else:
            i += 1

        length += 1
    return length


def encode_value(s):
    return len(s) + len(re.findall(r'["\\]', s)) + 2


string_code = sum(map(len, strings))
string_value = sum(map(str_value, strings))

print "Part 1:", string_code - string_value

encoded_value = sum(map(encode_value, strings))

print "Part 2:", encoded_value - string_code
