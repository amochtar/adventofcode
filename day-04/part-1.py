import re
from collections import Counter
from operator import itemgetter

with open("input.txt", "r") as f:
    rooms = [x.strip() for x in f.readlines()]

regex = re.compile(r'([a-z-]+)-(\d+)\[([a-z]+)\]')

count = 0
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
        count += sector_id
    else:
        print room
        print room_name, sector_id, checksum, validation, val

print count
