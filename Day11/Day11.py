with open('Input.txt', 'r') as f:
    data = [int(stone) for stone in f.read().split(' ')]


class Stone:
    def __init__(self, num: int):
        self.num = num


stones = set()
for stoneNum in data:
    stones.add(Stone(stoneNum))

# Part1
for i in range(25):
    print(i)
    newStones = set()
    for stone in stones:
        if stone.num == 0:
            stone.num = 1
        elif len(x := str(stone.num)) % 2 == 0:
            newStones.add(Stone(int(x[:len(x)//2])))
            stone.num = int(x[len(x)//2:])
        else:
            stone.num = stone.num * 2024
        newStones.add(stone)
    stones = newStones

print(len(stones))
