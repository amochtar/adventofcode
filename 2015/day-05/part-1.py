from collections import Counter
import re

f = open("input.txt", "r")
input = f.readlines()
strings = [x.strip() for x in input]

# strings = [
#     'ugknbfddgicrmopn',
#     'aaa',
#     'jchzalrnumimnmhp',
#     'haegwjzuvuyypxyu',
#     'dvszwmarrgswjxmb'
# ]

vowels = 'aeiou'
twice = re.compile(r'([a-z])\1')
ignore = re.compile(r'ab|cd|pq|xy')


def is_nice(s):
    counter = Counter(s)
    num_vowels = sum([counter[el] for el in counter if el in vowels])
    match_twice = twice.search(s)
    match_ignore = ignore.search(s)

    print s, num_vowels, match_twice is not None, match_ignore is None

    if num_vowels >= 3 and match_twice is not None and match_ignore is None:
        return True

    return False


print len([s for s in strings if is_nice(s)])
