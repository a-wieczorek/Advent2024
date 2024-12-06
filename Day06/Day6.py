with open('Input.txt', 'r') as f:
    data = f.read().split('\n')
    roomMap = [[col for col in row] for row in data if row]


class Guard:
    def __init__(self, row: int, col: int, aMap: list[list]):
        self.startRow = row
        self.startCol = col
        self.row = row
        self.col = col
        self.aMap = aMap
        self.history = []
        self.direction = '^'

    @property
    def visited(self) -> set[tuple]:
        return {(row, col) for row, col, _ in self.history}

    def step(self) -> bool:
        def check_out_of_room(row: int, col: int) -> bool:
            return row < 0 or row >= len(self.aMap) or col < 0 or col >= len(self.aMap[0])

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

        self.history.append((self.row, self.col, self.direction))
        while True:
            newCoords = get_new_coords()

            if check_out_of_room(newCoords[0], newCoords[1]):
                return False

            if self.aMap[newCoords[0]][newCoords[1]] != '#':
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
guard = Guard(guardStartRow, guardStartCol, roomMap)
inRoom = True
while inRoom:
    inRoom = guard.step()

visitedCoords = guard.visited
print(len(visitedCoords))

# Part2
possibleLoops = 0
counter = 0
for row, col in visitedCoords:
    counter += 1
    if row == guardStartRow and col == guardStartCol:
        continue
    newMap = [[col[:] for col in row] for row in roomMap[:]]
    newMap[row][col] = '#'
    guard = Guard(guardStartRow, guardStartCol, newMap)
    inRoom = True
    while inRoom:
        inRoom = guard.step()
        if guard.history[-1] in guard.history[:-1]:
            possibleLoops += 1
            break
    print(f"{counter}/{len(visitedCoords)}")
print(possibleLoops)
