with open('Input.txt', 'r') as f:
    data = [[int(col) for col in row] for row in f.read().split('\n')]


class Trailhead:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.summits = set()
        self.rating = 0
        self.find_summits(row, col)

    def find_summits(self, x: int, y: int):
        if data[x][y] == 9:
            self.summits.add((x, y))
            self.rating += 1
            return
        for deltaRow, deltaCol in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
            if (newX := x + deltaRow) in range(len(data)) and (newY := y + deltaCol) in range(len(data[0])):
                if data[newX][newY] - data[x][y] == 1:
                    self.find_summits(newX, newY)
        return

    @property
    def score(self):
        return len(self.summits)


trailheads = set()
for i, row in enumerate(data):
    for j, col in enumerate(row):
        if col == 0:
            trailheads.add(Trailhead(i, j))

# Part1
print(sum(trailhead.score for trailhead in trailheads))
# Part2
print(sum(trailhead.rating for trailhead in trailheads))
