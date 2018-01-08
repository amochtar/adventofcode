import re

input = "1113122113"

p = re.compile(r'(\d)\1*')


def look_and_say(input):
    result = ""
    for m in p.finditer(input):
        result += str(m.end()-m.start()) + m.group(1)

    return result


for i in range(40):
    input = look_and_say(input)

print "Part 1:", len(input)

for i in range(10):
    input = look_and_say(input)

print "Part 2:", len(input)
