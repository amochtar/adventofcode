def solve(input):
    recipes = [3, 7]
    first = 0
    second = 1

    for _ in range(input+10):
        s = recipes[first] + recipes[second]
        if s >= 10:
            recipes += [1, s-10]
        else:
            recipes.append(s)

        first = (first + 1 + recipes[first]) % len(recipes)
        second = (second + 1 + recipes[second]) % len(recipes)

    print(''.join(map(str, recipes[input:input+10])))


# solve(9)
# solve(5)
# solve(18)
# solve(2018)
solve(503761)
