import re

with open('Input.txt', 'r') as f:
    data = f.read().split('\n')

mapWidth = 101
mapHeight = 103


class Robot:
    def __init__(self, row: int, col: int, rowDelta: int, colDelta: int):
        self.row = row
        self.col = col
        self.rowDelta = rowDelta
        self.colDelta = colDelta

    def move(self):
        if (newRow := self.row + self.rowDelta) in range(mapHeight):
            self.row = newRow
        elif newRow >= mapHeight:
            self.row = newRow - mapHeight
        else:
            self.row = mapHeight + newRow

        if (newCol := self.col + self.colDelta) in range(mapWidth):
            self.col = newCol
        elif newCol >= mapWidth:
            self.col = newCol - mapWidth
        else:
            self.col = mapWidth + newCol
        #aMap = [['.'] * mapWidth for _ in range(mapHeight)]
        #aMap[self.row][self.col] = '1'
        #print('\n'.join([''.join(row) for row in aMap]))
        #print('\n')
        return

    @property
    def quadrant(self):
        if self.row < mapHeight // 2 and self.col < mapWidth // 2:
            return 1
        elif self.row >= -(-mapHeight // 2) and self.col < mapWidth // 2:
            return 2
        elif self.row < mapHeight // 2 and self.col >= -(-mapWidth // 2):
            return 3
        elif self.row >= -(-mapHeight // 2) and self.col >= -(-mapWidth // 2):
            return 4
        else:
            return 'mid'


robots = set()
robots2 = set()
for row in data:
    x, y, xDelta, yDelta = [int(num) for num in re.findall('-?\d+', row)]
    robots.add(Robot(y, x, yDelta, xDelta))
    robots2.add(Robot(y, x, yDelta, xDelta))

# Part1
quadrants = {1: 0, 2: 0, 3: 0, 4: 0, 'mid': 0}
for robot in robots:
    for i in range(100):
        robot.move()
    quadrants[robot.quadrant] += 1

print(quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4])

# Part2
for i in range(7916):
    for robot in robots2:
        robot.move()

aMap = [[' '] * mapWidth for _ in range(mapHeight)]
for robot in robots2:
    aMap[robot.row][robot.col] = '*'
print(str(i + 1) + '\n' + '\n'.join([''.join(row) for row in aMap]))
x = '\n'.join([''.join(row) for row in aMap])


