import re

marker = re.compile(r'(\((\d+)x(\d+)\))')


def decoded_length(input):
    match = marker.search(input)
    if match:
        i = match.start(1)
        j = match.end(1)
        n = int(match.group(2))
        t = int(match.group(3))
        return i + (t * decoded_length(input[j:j + n])) + decoded_length(input[j + n:])
    else:
        return len(input)


with open("input.txt", "r") as f:
    input = f.read()
    print decoded_length(input)
