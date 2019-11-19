import re

f = open('input.txt', 'r')
input = f.read()

two_pairs = re.compile(r'([a-z])\1[a-z]*(?!\1)([a-z])\2')
confusing = re.compile(r'[iol]')


def has_increasing_straight(password):
    for i in range(len(password) - 2):
        if (ord(password[i]) == ord(password[i+1]) - 1) and (ord(password[i]) == ord(password[i+2]) - 2):
            return True
    return False


def is_valid(password):
    if not has_increasing_straight(password):
        return False
    # if confusing.findall(password):
    #     return False
    if not two_pairs.search(password):
        return False
    return True


def increment(password):
    chars = [ord(c) for c in password]
    chars[-1] += 1
    if chars[-1] in [ord('i'), ord('o'), ord('l')]:
        chars[-1] += 1

    for i in reversed(range(len(chars))):
        if chars[i] > ord('z'):
            chars[i] = ord('a')
            if i > 0:
                chars[i-1] += 1
                if chars[i-1] in [ord('i'), ord('o'), ord('l')]:
                    chars[i-1] += 1

    return ''.join([chr(c) for c in chars])


password = increment(input)
while not is_valid(password):
    password = increment(password)

print "Part 1:", password

password = increment(password)
while not is_valid(password):
    password = increment(password)

print "Part 2:", password
