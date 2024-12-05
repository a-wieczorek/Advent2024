with open('Input.txt', 'r') as f:
    data = f.read().split('\n')

rules = [rule.split('|') for rule in data if '|' in rule]
updates = [update.split(',') for update in data if ',' in update]

ruleDict = {}
for rule in rules:
    ruleDict.setdefault(rule[0], set()).add(rule[1])

# Part1
correctMiddlesList = []
incorrectList = []
for update in updates:
    isCorrect = True
    for i, page in enumerate(update):
        if any(rulePage in update[:i] for rulePage in ruleDict.get(page, [])):
            isCorrect = False
            break
    if isCorrect:
        correctMiddlesList.append(update[len(update)//2])
    else:
        incorrectList.append(update)
print(sum([int(page) for page in correctMiddlesList]))

# Part2
correctedMiddlesList = []
for update in incorrectList:
    isIncorrect = True
    while isIncorrect:
        i = 0
        while i < len(update):
            isIncorrect = False
            page = update[i]
            i += 1
            for subPage in ruleDict.get(page, []):
                if subPage in update[:i]:
                    update.append(update.pop(update.index(subPage)))
                    isIncorrect = True
                    i = 0
                    break
    correctedMiddlesList.append(update[len(update) // 2])
print(sum([int(page) for page in correctedMiddlesList]))
