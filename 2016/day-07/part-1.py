import re

with open("input.txt", "r") as f:
    ips = [x.strip() for x in f.readlines()]

abba = re.compile(r'([a-z])(?!\1)([a-z])\2\1')
abba_in_hyper = re.compile(r'\[[^]]*?([a-z])(?!\1)([a-z])\2\1[^[]*?\]')

print sum([1 for ip in ips if abba.search(ip) and not abba_in_hyper.search(ip)])
