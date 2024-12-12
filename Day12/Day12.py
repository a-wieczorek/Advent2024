with open('Input.txt', 'r') as f:
    data = [[col for col in row] for row in f.read().split('\n')]


class Region:
    def __init__(self, startX: int, startY: int, plant: str):
        self.perimeter = 0
        self.sides = 0
        self.locations = set()
        self.plant = plant
        self.chart_region(startX, startY)

    def chart_region(self, x: int, y: int):
        self.locations.add((x, y))
        for deltaRow, deltaCol in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
            if (newX := x + deltaRow) in range(len(data)) and (newY := y + deltaCol) in range(len(data[0])):
                if data[newX][newY] == self.plant:
                    if (newX, newY) not in self.locations:
                        self.chart_region(newX, newY)
                    continue
            self.perimeter += 1
        return

    @property
    def area(self):
        return len(self.locations)


regions = set()
for i, row in enumerate(data):
    for j, col in enumerate(row):
        if not any((i, j) in exploredLocations for exploredLocations in [region.locations for region in regions]):
            regions.add(Region(i, j, col))

# Part1
print(sum(region.area * region.perimeter for region in regions))


# Part2
def check_existing_side(sides: list, directionCondition: tuple[int, int], direction: str):
    if directionCondition not in region.locations:
        for i, side in enumerate(sides):
            if (direction == 'W/E' and (row - 1, col) in side) or (direction == 'N/S' and (row, col - 1) in side):
                sides[i].append((row, col))
                return sides
        sides.append([(row, col)])
    return sides


for region in regions:
    westSides, eastSides, northSides, southSides = [], [], [], []
    for row, col in sorted(region.locations):
        westSides = check_existing_side(westSides, (row, col - 1), 'W/E')
        eastSides = check_existing_side(eastSides, (row, col + 1), 'W/E')
        northSides = check_existing_side(northSides, (row - 1, col), 'N/S')
        southSides = check_existing_side(southSides, (row + 1, col), 'N/S')
    region.sides += len(westSides) + len(eastSides) + len(northSides) + len(southSides)
print(sum(region.area * region.sides for region in regions))
