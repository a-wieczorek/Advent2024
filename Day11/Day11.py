from collections import defaultdict

with open('Input.txt', 'r') as f:
    data = [int(stone) for stone in f.read().split(' ')]


stones = set()
amounts = defaultdict(int)
for stoneNum in data:
    amounts[stoneNum] += 1
    stones.add(stoneNum)

cache = {}

for i in range(75):
    newAmounts = defaultdict(int)
    newStones = set()
    for stone in stones:
        if stone in cache:
            newNum = cache[stone]['newNum']
            spawnsCopy = cache[stone]['spawnsCopy']
            newStoneNum = cache[stone]['newStoneNum']
        else:
            spawnsCopy = False
            newStoneNum = None
            if stone == 0:
                newNum = 1
            elif len(x := str(stone)) % 2 == 0:
                spawnsCopy = True
                newNum = int(x[:len(x)//2])
                newStoneNum = int(x[len(x)//2:])
            else:
                newNum = stone * 2024
            cache[stone] = {'newNum': newNum, 'spawnsCopy': spawnsCopy, 'newStoneNum': newStoneNum}
        newStones.add(newNum)
        newAmounts[newNum] += amounts[stone]
        if spawnsCopy:
            newStones.add(newStoneNum)
            newAmounts[newStoneNum] += amounts[stone]
    stones = newStones
    amounts = newAmounts

    # Part1
    if i == 24:
        print(sum(amounts[stone] for stone in stones))
# Part2
print(sum(amounts[stone] for stone in stones))
