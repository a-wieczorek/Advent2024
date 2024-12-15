with open('Input.txt', 'r') as f:
    data = f.read().split('\n')


class MapElem:
    def __init__(self, row: int, col: int, symbol: str, col2: int = None):
        self.row = row
        self.col = col
        self.col2 = col2
        self.symbol = symbol

    def __repr__(self) -> str:
        return self.symbol

    def move(self, direction: str) -> None:
        rowDelta, colDelta = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[direction]
        newRow, newCol = self.row + rowDelta, self.col + colDelta
        if aMap[newRow][newCol].symbol != '.':
            aMap[newRow][newCol].move(direction)

        aMap[newRow][newCol] = aMap[self.row][self.col]
        aMap[self.row][self.col] = MapElem(self.row, self.col, '.')
        self.row = newRow
        self.col = newCol

    def isMovable(self, direction: str, isPart2: bool = False) -> bool:
        rowDelta, colDelta = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[direction]
        newRow, newCol = self.row + rowDelta, self.col + colDelta
        if self.symbol == '@' or not isPart2:
            if aMap[newRow][newCol].symbol == '#' \
                    or aMap[newRow][newCol].symbol == 'O' and not aMap[newRow][newCol].isMovable(direction, isPart2):
                return False
            return True
        else:
            newCol2 = self.col2 + colDelta
            if direction in ['^', 'v']:
                if aMap[newRow][newCol].symbol == '#' or aMap[newRow][self.col2 + colDelta].symbol == '#' \
                        or aMap[newRow][newCol].symbol == 'O' and not aMap[newRow][newCol].isMovable(direction, isPart2) \
                        or aMap[newRow][newCol2].symbol == 'O' and not aMap[newRow][newCol2].isMovable(direction, isPart2):
                    return False
            elif direction == '<':
                if aMap[newRow][newCol].symbol == '#' \
                        or aMap[newRow][newCol].symbol == 'O' and not aMap[newRow][newCol].isMovable(direction, isPart2):
                    return False
            else:
                if aMap[newRow][newCol2].symbol == '#' \
                        or aMap[newRow][newCol2].symbol == 'O' and not aMap[newRow][newCol2].isMovable(direction, isPart2):
                    return False
            return True

    def move2(self, direction: str) -> None:
        rowDelta, colDelta = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[direction]
        newRow, newCol = self.row + rowDelta, self.col + colDelta

        if self.symbol == '@':
            if aMap[newRow][newCol].symbol != '.':
                aMap[newRow][newCol].move2(direction)
            aMap[newRow][newCol] = aMap[self.row][self.col]
            aMap[self.row][self.col] = MapElem(self.row, self.col, '.')
            self.row = newRow
            self.col = newCol
        else:
            newCol2 = self.col2 + colDelta
            if direction != '>':
                if aMap[newRow][newCol].symbol != '.':
                    aMap[newRow][newCol].move2(direction)
            if direction != '<':
                if aMap[newRow][newCol2].symbol != '.':
                    aMap[newRow][newCol2].move2(direction)

            aMap[newRow][newCol] = aMap[self.row][self.col]
            aMap[newRow][newCol2] = aMap[self.row][self.col]
            if direction != '<':
                aMap[self.row][self.col] = MapElem(self.row, self.col, '.')
            if direction != '>':
                aMap[self.row][self.col2] = MapElem(self.row, self.col2, '.')
            aMap[newRow][newCol].row = newRow
            aMap[newRow][newCol].col = newCol
            aMap[newRow][newCol].col2 = newCol2

    @property
    def GPS(self):
        return (100 * self.row) + self.col


# Part1
partialMap = []
instructions = ''
for row in data:
    if row.startswith('#'):
        partialMap.append(list(row[:]))
    elif row:
        instructions += row

aMap: list[list[MapElem]] = []
for i, row in enumerate(partialMap):
    aMap.append([])
    for j, col in enumerate(row):
        if partialMap[i][j] == '@':
            submarine = MapElem(i, j, '@')
            aMap[i].append(submarine)
        else:
            aMap[i].append(MapElem(i, j, col))

for sign in instructions:
    if submarine.isMovable(sign):
        submarine.move(sign)
print(sum([sum([col.GPS for col in row if col.symbol == 'O']) for row in aMap]))


# Part2
partialMap = []
for row in data:
    row = row.replace('#', '##').replace('.', '..').replace('@', '@.').replace('O', '[]')
    if row.startswith('#'):
        partialMap.append(list(row[:]))

aMap: list[list[MapElem]] = []
for i, row in enumerate(partialMap):
    aMap.append([])
    for j, col in enumerate(row):
        if col == '@':
            submarine = MapElem(i, j, '@')
            aMap[i].append(submarine)
        elif col == '[':
            obstacle = MapElem(i, j, 'O', col2=j+1)
            aMap[i].append(obstacle)
            aMap[i].append(obstacle)
        elif col in ['.', '#']:
            aMap[i].append(MapElem(i, j, col))

for sign in instructions:
    if submarine.isMovable(sign, isPart2=True):
        submarine.move2(sign)
print(sum([sum([col.GPS for col in set(row) if col.symbol == 'O']) for row in aMap]))
