with open('Input.txt', 'r') as f:
    data = [machine for machine in f.read().split('\n\n')]

machines = []
for machine in data:
    machineDict = {}
    machineLines = machine.split('\n')
    for i, line in enumerate(machineLines):
        val = line
        for mess in ['Button A: ', 'Button B: ', 'Prize: ', 'X', 'Y', '+', '=']:
            val = val.replace(mess, '')
        val = val.split(', ')
        machineLines[i] = [int(val[0]), int(val[1])]
    machineDict['A'] = {'X': machineLines[0][0], 'Y': machineLines[0][1]}
    machineDict['B'] = {'X': machineLines[1][0], 'Y': machineLines[1][1]}
    machineDict['Prize'] = {'X': machineLines[2][0], 'Y': machineLines[2][1]}
    machines.append(machineDict)


def count_buttons(machines: list[dict], isPart2: bool = False):
    total = 0
    for machine in machines:
        if isPart2:
            machine['Prize']['X'] += 10000000000000
            machine['Prize']['Y'] += 10000000000000
        a = [machine['Prize']['X'] / machine['A']['X'], machine['B']['X']/machine['A']['X']]
        b = (machine['Prize']['Y'] - (machine['A']['Y'] * a[0])) / (machine['B']['Y'] - (machine['A']['Y'] * a[1]))
        a = a[0] - a[1]*b
        a = round(a)
        b = round(b)
        if a * machine['A']['X'] + b * machine['B']['X'] == machine['Prize']['X'] \
            and a * machine['A']['Y'] + b * machine['B']['Y'] == machine['Prize']['Y']\
                and ((a <= 100 and b <= 100) or isPart2):
            total += int(3*a + b)
    return total


print(count_buttons(machines))
print(count_buttons(machines, True))
