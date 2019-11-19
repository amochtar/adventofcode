with open('input.txt', 'r') as f:
    input = f.readlines()

target = 150

jars = [int(line) for line in input]


def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial

    if partial_sum > target:
        return

    for i, n in enumerate(numbers):
        remaining = numbers[i+1:]
        for subset in subset_sum(remaining, target, partial+[n], partial_sum+n):
            yield subset


combis = list(subset_sum(jars, target))
print "Part 1:", len(combis)

min_jars = min([len(c) for c in combis])
print "Part 2:", len([c for c in combis if len(c) == min_jars])
