with open('Input.txt', 'r') as f:
    data = [[col for col in row] for row in f.read().split('\n') if row]


def check_part1(x, y, xDelta, yDelta) -> bool:
    if x + xDelta * 3 < 0 or x + xDelta * 3 >= len(data) \
            or y + yDelta * 3 < 0 or y + yDelta * 3 >= len(data[0]):
        return False
    else:
        if data[x + xDelta][y + yDelta] == 'M' \
                and data[x + xDelta * 2][y + yDelta * 2] == 'A' \
                and data[x + xDelta * 3][y + yDelta * 3] == 'S':
            return True
        else:
            return False


def check_part2(x, y, xDelta, yDelta):
    if data[x + xDelta][y + yDelta] + data[x - xDelta][y - yDelta] in ['MS', 'SM'] \
            and data[x + yDelta][y - xDelta] + data[x - yDelta][y + xDelta] in ['MS', 'SM']:
        return True
    else:
        return False


# Part1
count1 = 0
count2 = 0
for i, row in enumerate(data):
    for j, col in enumerate(row):
        # Part 1
        if col == 'X':
            checks = [check_part1(i, j, rowDirection, colDirection) for rowDirection, colDirection in
                      [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]]
            count1 += sum(checks)
        # Part 2
        if col == 'A' and 1 <= i <= len(data) - 2 and 1 <= j <= len(row) - 2:
            checks = [check_part2(i, j, rowDirection, colDirection) for rowDirection, colDirection in
                      [(1, 1), (1, -1)]]
            count2 += int(sum(checks) / 2)

print(count1)
print(count2)