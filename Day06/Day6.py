with open('Input.txt', 'r') as f:
    data = f.read().split('\n')
    roomMap = [[col for col in row] for row in data if row]


class Guard:
    def __init__(self, row: int, col: int):
        self.startRow = row
        self.startCol = col
        self.row = row
        self.col = col
        self.history = set()
        self.direction = '^'

    @property
    def visited(self) -> set[tuple]:
        return {(row, col) for row, col, _ in self.history}

    def step(self) -> bool:

        def turn() -> None:
            if self.direction == '^':
                self.direction = '>'
            elif self.direction == '>':
                self.direction = 'v'
            elif self.direction == 'v':
                self.direction = '<'
            else:
                self.direction = '^'
            return

        def get_new_coords() -> tuple:
            if self.direction == '^':
                coords = (self.row - 1, self.col)
            elif self.direction == '>':
                coords = (self.row, self.col + 1)
            elif self.direction == 'v':
                coords = (self.row + 1, self.col)
            else:
                coords = (self.row, self.col - 1)
            return coords

        self.history.add((self.row, self.col, self.direction))
        while True:
            newCoords = get_new_coords()

            if newCoords[0] not in range(0, len(roomMap)) or newCoords[1] not in range(0, len(roomMap[0])):
                return False

            if roomMap[newCoords[0]][newCoords[1]] != '#':
                self.row, self.col = newCoords
                return True
            else:
                turn()


# Part1
guardStartRow = 0
guardStartCol = 0
for i, row in enumerate(data):
    if '^' in row:
        guardStartRow = i
        guardStartCol = row.index('^')
        break
roomMap[guardStartRow][guardStartCol] = '.'
guard = Guard(guardStartRow, guardStartCol)
inRoom = True
while inRoom:
    inRoom = guard.step()

visitedCoords = guard.visited
print(len(visitedCoords))

# Part2 ~10sec
possibleLoops = 0
counter = 0
for row, col in visitedCoords:
    counter += 1
    if row == guardStartRow and col == guardStartCol:
        continue
    roomMap[row][col] = '#'
    guard = Guard(guardStartRow, guardStartCol)
    inRoom = True
    while inRoom:
        inRoom = guard.step()
        if inRoom and (guard.row, guard.col, guard.direction) in guard.history:
            possibleLoops += 1
            break
    roomMap[row][col] = '.'
    print(f"{counter}/{len(visitedCoords)}")
print(f'\nPart1\n{len(visitedCoords)}\n\nPart2\n{possibleLoops}')
