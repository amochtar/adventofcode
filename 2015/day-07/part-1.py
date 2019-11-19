f = open("input.txt", "r")
input = f.readlines()
circuits = [x.strip() for x in input]

wires = {}
for circuit in circuits:
    gate, wire = circuit.split(' -> ')
    wires[wire.strip()] = gate.strip()

results = {}


def calculate(w):
    # print results
    try:
        return int(w)
    except ValueError:
        pass

    try:
        return results[w]
    except KeyError:
        pass

    # print "wire[%s] = %s" % (w, wires[w])
    parts = wires[w].split()
    # print parts
    if len(parts) == 1:
        if parts[0].isdigit():
            results[w] = int(parts[0])
        else:
            results[w] = calculate(parts[0])
    elif "NOT" in parts:
        results[w] = ~ calculate(parts[1])
    elif "RSHIFT" in parts:
        results[w] = calculate(parts[0]) >> int(parts[2])
    elif "LSHIFT" in parts:
        results[w] = calculate(parts[0]) << int(parts[2])
    elif "OR" in parts:
        results[w] = calculate(parts[0]) | calculate(parts[2])
    elif "AND" in parts:
        results[w] = calculate(parts[0]) & calculate(parts[2])
    return results[w]

a = calculate('a')
print "Part 1:", a
wires['b'] = str(a)
results={}
print "Part 2:", calculate('a')
