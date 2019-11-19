import re
import hashlib

triples_pattern = re.compile(r'(.)\1\1')
quintuples_pattern = re.compile(r'(.)\1\1\1\1')


def has_quintuple(c, i):
    for j in range(i, i+1000):
        md5 = get_hash(j)
        if c in quintuples_pattern.findall(md5):
            return True
    return False


def get_hash(i):
    if i not in hashes:
        h = input + str(i)
        for x in range(2017):
            h = hashlib.md5(h).hexdigest()
        hashes[i] = h
    return hashes[i]


with open('input.txt', 'r') as f:
    input = f.read()

hashes = {}
index = 0
indices = []
while len(indices) < 64:
    md5 = get_hash(index)
    triples_match = triples_pattern.search(md5)
    if triples_match and has_quintuple(triples_match.group(1), index+1):
        indices.append(index)

    index += 1

print indices[-1], indices
