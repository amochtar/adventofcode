from collections import defaultdict

with open("input.txt", "r") as f:
    input = [x.strip() for x in f.readlines()]

instructions = {}
bots = defaultdict(list)
outputs = {}

for i in input:
    parts = i.split()
    if parts[0] == 'value':
        bots[parts[5]].append(int(parts[1]))
    elif parts[2] == 'gives':
        instructions[parts[1]] = {
            'low': (parts[5], parts[6]),
            'high': (parts[-2], parts[-1])
        }

has_bots = False
has_outputs = False

while not (has_bots and has_outputs):
    bot = {k: v for k, v in bots.iteritems() if len(v) > 1}
    for name, values in bot.iteritems():
        if 17 in values and 61 in values:
            print "Part 1:", name
            has_bots = True

        x = instructions[name]
        high = x['high']
        if high[0] == 'bot':
            bots[high[1]].append(max(values))
        else:
            outputs[high[1]] = max(values)
        low = x['low']
        if low[0] == 'bot':
            bots[low[1]].append(min(values))
        else:
            outputs[low[1]] = min(values)
        bots[name] = []

        try:
            part2 = outputs['0'] * outputs['1'] * outputs['2']
            print "Part 2:", part2
            has_outputs = True
        except KeyError:
            pass
