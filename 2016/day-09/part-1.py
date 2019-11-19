with open("input.txt", "r") as f:
    input = f.read()

decoded = ""
i = 0
while i < len(input):
    if input[i] == '(':
        j = input.index(')', i)
        n, t = map(int, input[i + 1:j].split('x'))
        decoded += input[j + 1:j + 1 + n] * t
        i = j + n + 1
    else:
        decoded += input[i]
        i += 1

print len(decoded)
