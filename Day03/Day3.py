import re

with open('Input.txt', 'r') as f:
    data = f.read()

commands = re.findall("(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))", data)

# Part1
result = 0
for mul in [command for command in commands if 'mul' in command]:
    num1, num2 = re.findall('([0-9]+)', mul)
    result += int(num1) * int(num2)
print(result)

# Part2
result = 0
ignore = False
for command in commands:
    if command == "don't()":
        ignore = True
        continue
    elif command == "do()":
        ignore = False
        continue
    if not ignore:
        num1, num2 = re.findall('([0-9]+)', command)
        result += int(num1) * int(num2)
print(result)