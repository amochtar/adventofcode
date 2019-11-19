def next_code(code):
    return (code * 252533) % 33554393


def num_codes(row, column):
    return sum(range(row + column - 1)) + column


row = 2981
column = 3075
code = 20151125

for i in range(1, num_codes(row, column)):
    code = next_code(code)

print code
