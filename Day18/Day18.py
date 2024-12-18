import sys
import threading

with open('Input.txt', 'r') as f:
    data = [(int(row.split(',')[0]), int(row.split(',')[1])) for row in f.read().split('\n')]

aMap = costMap = [['.' for col in range(71)] for row in range(71)]
costMap = [[10000000 for col in range(71)] for row in range(71)]

i = 0
for byteCol, byteRow in data:
    i += 1
    aMap[byteRow][byteCol] = '#'
    if i == 1023:
        break

me = (0, 0)
routes = {}


def find_routes(row: int, col: int, route: list, cost: int, rec):
    print(rec)
    if row == col == len(aMap) - 1:
        routes[cost] = route
        return
    for deltaRow, deltaCol in {(-1, 0), (1, 0), (0, 1), (0, -1)}:
        newRow = row + deltaRow
        newCol = col + deltaCol
        if newRow in range(len(aMap)) and newCol in range(len(aMap[0])) and aMap[newRow][newCol] != '#' and (newRow, newCol) not in route:
            newCost = cost + 1
            if newCost < costMap[newRow][newCol]:
                costMap[newRow][newCol] = newCost
                find_routes(newRow, newCol, route + [(newRow, newCol)], newCost, rec + 1)


def start():
    find_routes(0, 0, [(0, 0)], 0, 0)
    print(min(routes.keys()))


if __name__ == '__main__':
    sys.setrecursionlimit(50000)
    threading.stack_size(200000000)
    thread = threading.Thread(target=start)
    thread.start()
