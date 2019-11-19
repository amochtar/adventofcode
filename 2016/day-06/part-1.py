from collections import Counter
from collections import defaultdict

with open("input.txt", "r") as f:
    messages = [x.strip() for x in f.readlines()]

d = defaultdict(Counter)
for message in messages:
    for i in range(len(message)):
        d[i][message[i]] += 1

print 'Part 1:', ''.join([value.most_common()[0][0] for key, value in d.iteritems()])
print 'Part 2:', ''.join([value.most_common()[-1][0] for key, value in d.iteritems()])
