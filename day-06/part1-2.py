def highest_allocation(banks):
    return max(enumerate(banks), key=lambda x: x[1])


def distribute(banks):
    num_banks = len(banks)
    idx, blocks = highest_allocation(banks)
    banks[idx] = 0
    for i in range(blocks):
        idx = (idx+1) % num_banks
        banks[idx] += 1
    return banks


def solve(banks):
    visited = set()
    visited.add(tuple(banks))
    count = 0
    while True:
        banks = distribute(banks)
        if tuple(banks) in visited:
            break
        visited.add(tuple(banks))
        count += 1
    return len(visited), banks


with open('input.txt', 'r') as f:
    banks = list(map(int, f.read().split()))

cycles, banks = solve(banks)
print("Part 1:", cycles)
cycles, banks = solve(banks)
print("Part 2:", cycles)
