def solve(input):
    recipes = [3, 7]
    first = 0
    second = 1

    iterations = 0
    while True:
        f = recipes[first]
        s = recipes[second]

        new_recipes = f+s
        if new_recipes >= 10:
            recipes += [1, new_recipes-10]
        else:
            recipes.append(new_recipes)

        first = (first + 1 + f) % len(recipes)
        second = (second + 1 + s) % len(recipes)

        iterations += 1
        if iterations % 1000000 == 0:
            r = ''.join(map(str, recipes))
            try:
                i = r.index(input)
                if i > 0:
                    print(i)
                    break
            except ValueError:
                pass


# solve('51589')
# solve('01245')
# solve('92510')
# solve('59414')
solve('503761')
