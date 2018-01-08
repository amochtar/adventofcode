from collections import Counter
import re

f = open("input.txt", "r")
input = f.readlines()
strings = [x.strip() for x in input]

twice = re.compile(r'([a-z][a-z])[a-z]*\1')
repeat = re.compile(r'([a-z])[a-z]\1')


def is_nice(s):
    match_twice = twice.search(s)
    match_repeat = repeat.search(s)

    print s, match_twice is not None, match_repeat is not None

    if match_twice is not None and match_repeat is not None:
        return True

    return False


print len([s for s in strings if is_nice(s)])
