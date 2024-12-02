with open('Input.txt', 'r') as f:
    data = [[int(num) for num in row.split(' ')] for row in f.read().split('\n') if row]


def analyse_reports(data: list) -> (int, list):
    safeReps = []
    retryRows = []
    for row in data:
        state = 'start'
        isSafe = True
        for i in range(1, len(row)):
            prev = row[i-1]
            curr = row[i]
            if not 1 <= abs(int(prev) - int(curr)) <= 3:
                isSafe = False
                retryRows.append(row[:max(i - 2, 0)] + row[i - 1:])
                retryRows.append(row[:i-1] + row[i:])
                retryRows.append(row[:i] + row[i+1:])
                break
            if curr < prev:
                if state == 'increasing':
                    isSafe = False
                    retryRows.append(row[:max(i - 2, 0)] + row[i - 1:])
                    retryRows.append(row[:i - 1] + row[i:])
                    retryRows.append(row[:i] + row[i+1:])
                    break
                state = 'decreasing'
            else:
                if state == 'decreasing':
                    isSafe = False
                    retryRows.append(row[:max(i - 2, 0)] + row[i - 1:])
                    retryRows.append(row[:i - 1] + row[i:])
                    retryRows.append(row[:i] + row[i+1:])
                    break
                state = 'increasing'

        if isSafe:
            safeReps.append(1)
        else:
            safeReps.append(0)
    return safeReps, retryRows


res, retry = analyse_reports(data)
print(f'{sum(res)}')
res2, _ = analyse_reports(retry)
out = [max(res2[i:i + 3]) for i in range(0, len(res2), 3)]
print(f'{sum(res) + sum(out)}')

