import json

with open('input.txt', 'r') as f:
    j = json.load(f)


def sum_numbers(j_obj):
    if isinstance(j_obj, dict):
        return sum([sum_numbers(v) for _, v in j_obj.iteritems()])
    elif isinstance(j_obj, list):
        return sum(map(sum_numbers, j_obj))
    elif isinstance(j_obj, int):
        return j_obj
    else:
        return 0


def sum_numbers_2(j_obj):
    if isinstance(j_obj, dict):
        if 'red' in j_obj.values():
            return 0
        else:
            return sum([sum_numbers_2(v) for _, v in j_obj.iteritems()])
    elif isinstance(j_obj, list):
        return sum(map(sum_numbers_2, j_obj))
    elif isinstance(j_obj, int):
        return j_obj
    else:
        return 0

print "Part 1:", sum_numbers(j)
print "Part 2:", sum_numbers_2(j)
