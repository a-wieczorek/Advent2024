with open('Input.txt', 'r') as f:
    data = f.read().split('\n')

dataLeft, dataRight = [], []
for row in data:
    left, right = row.split('   ')
    dataLeft.append(left)
    dataRight.append(right)

# Part1
distances = [abs(int(left)-int(right)) for left, right in zip(sorted(dataLeft), sorted(dataRight))]
print(sum(distances))

# Part2
similarities = [int(num)*dataRight.count(num) for num in dataLeft]
print(sum(similarities))
