with open('Input.txt', 'r') as f:
    dataRaw = f.read()
    data = dataRaw.split('\n')


class Frequency:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def coord_distance(self, otherFrequency: 'Frequency') -> tuple[int, int]:
        return otherFrequency.row - self.row, otherFrequency.col - self.col


frequencySymbols = set(dataRaw.replace('\n', '').replace('.', ''))

antinodesPart1 = set()
antinodesPart2 = set()
for frequencySymbol in frequencySymbols:
    frequencies = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col == frequencySymbol:
                frequencies.append(Frequency(i, j))

    for i in range(len(frequencies)):
        for j in range(i + 1, len(frequencies)):
            # Part1
            rowDistance, colDistance = frequencies[i].coord_distance(frequencies[j])
            if (x := frequencies[i].row + rowDistance * 2) in range(0, len(data)) \
                    and (y := frequencies[i].col + colDistance * 2) in range(0, len(data[0])):
                antinodesPart1.add((x, y))

            if (x := frequencies[i].row - rowDistance) in range(0, len(data)) \
                    and (y := frequencies[i].col - colDistance) in range(0, len(data[0])):
                antinodesPart1.add((x, y))

            # Part2
            antinodesPart2.add((frequencies[i].row, frequencies[i].col))
            k = 1
            while True:
                if (x := frequencies[i].row + (rowDistance * k)) in range(0, len(data)) \
                        and (y := frequencies[i].col + (colDistance * k)) in range(0, len(data[0])):
                    antinodesPart2.add((x, y))
                    k += 1
                    continue
                break

            k = 1
            while True:
                if (x := frequencies[i].row - (rowDistance * k)) in range(0, len(data)) \
                        and (y := frequencies[i].col - (colDistance * k)) in range(0, len(data[0])):
                    antinodesPart2.add((x, y))
                    k += 1
                    continue
            break


print(len(antinodesPart1))
print(len(antinodesPart2))
