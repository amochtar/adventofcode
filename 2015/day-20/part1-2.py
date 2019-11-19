import math


def factors(n):
    small_divisors = [i for i in xrange(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return sorted(small_divisors + large_divisors)


def presents(f):
    return sum(f) * 10


def presents2(f, h):
    return sum(fact for fact in f if h / fact <= 50) * 11


input = 33100000
part_1 = part_2 = 0
houses = 0
while part_1 == 0 or part_2 == 0:
    houses += 1
    f = factors(houses)
    if part_1 == 0:
        if presents(f) >= input:
            part_1 = houses
    if part_2 == 0:
        if presents2(f, houses) >= input:
            part_2 = houses

print part_1, part_2
