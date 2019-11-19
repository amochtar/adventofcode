import re
from collections import Counter
from operator import itemgetter

with open("input.txt", "r") as f:
    rooms = [x.strip() for x in f.readlines()]

regex = re.compile(r'([a-z-]+)-(\d+)\[([a-z]+)\]')


def decrypt(message, key):
    key = key % 26
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated


for room in rooms:
    match = regex.match(room)
    room_name = match.group(1).replace('-', '')
    sector_id = int(match.group(2))
    checksum = match.group(3)
    validation = Counter(room_name).most_common()
    validation = sorted(validation, key=itemgetter(0))
    validation = sorted(validation, key=itemgetter(1), reverse=True)
    val = "".join([v[0] for v in validation])[:5]
    if val == checksum:
        decrypted_room_name = decrypt(match.group(1).replace('-', ' '), sector_id)
        if "north" in decrypted_room_name:
            print decrypted_room_name, sector_id
