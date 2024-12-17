import sys
import threading

with open('Input.txt', 'r') as f:
    data = [[col for col in row] for row in f.read().split('\n')]

costMap = [[10000000 for col in range(len(data[0]))] for row in range(len(data))]


class Reindeer:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.routes = {}
        self.find_routes(row, col, 'E', [(row,col)], 0, 0)

    def find_routes(self, row: int, col: int, direction: str, route: list, cost: int, rec):
        print(rec)
        turns = {
            'E': {'E': 0, 'N': 1, 'S': 1, 'W': 2},
            'S': {'S': 0, 'E': 1, 'W': 1, 'N': 2},
            'W': {'W': 0, 'N': 1, 'S': 1, 'E': 2},
            'N': {'N': 0, 'E': 1, 'W': 1, 'S': 2}
        }
        if data[row][col] == 'E':
            if self.routes.get(cost):
                self.routes[cost] += route
                return
            self.routes[cost] = route
            return
        for deltaRow, deltaCol, newDirection in {(-1, 0, 'N'), (1, 0, 'S'), (0, 1, 'E'), (0, -1, 'W')}:
            newRow = row + deltaRow
            newCol = col + deltaCol
            if data[newRow][newCol] != '#' and (newRow, newCol) not in route:
                newCost = cost + 1 + turns[direction][newDirection] * 1000
                if newCost <= costMap[newRow][newCol]:
                    costMap[newRow][newCol] = newCost
                    self.find_routes(newRow, newCol, newDirection, route + [(newRow, newCol)], newCost, rec + 1)


def start():
    reindeer = (0, 0)
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col == 'S':
                reindeer = Reindeer(i, j)
                break
    print(min(reindeer.routes.keys()))


if __name__ == '__main__':
    sys.setrecursionlimit(50000)  # I see no god up here, other than me
    threading.stack_size(200000000)  # I see no god up here, other than me
    thread = threading.Thread(target=start)
    thread.start()
