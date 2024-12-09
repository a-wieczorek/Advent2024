with open('Input.txt', 'r') as f:
    data = f.read()


class File:
    def __init__(self, fileID: int, locations: list):
        self.fileID = fileID
        self.locations = locations

    def checksum_value(self):
        return self.fileID * sum(self.locations)


class FreeSpace:
    def __init__(self, locations: list):
        self.locations = locations


def gen_blocks() -> tuple[list, list]:
    files = []
    freeSpaces = []
    location = 0
    for i, block in enumerate(data):
        block = int(block)
        if i % 2 == 0:
            files.append(File(i // 2, list(range(location, location + block))))
        else:
            freeSpaces.append(FreeSpace(list(range(location, location + block))))
        location += block
    return files, freeSpaces


# Part1
files, freeSpaces = gen_blocks()
freeLocations = []
for freeSpace in freeSpaces:
    freeLocations += freeSpace.locations

for file in reversed(files):
    for i in reversed(range(len(file.locations))):
        if not freeLocations or file.locations[i] < freeLocations[0]:
            break
        file.locations[i] = freeLocations.pop(0)
print(sum({file.checksum_value() for file in files}))

# Part2
files, freeSpaces = gen_blocks()
for file in reversed(files):
    for freeSpace in freeSpaces:
        if len(file.locations) <= len(freeSpace.locations):
            if freeSpace.locations[0] >= file.locations[0]:
                break
            for j in range(len(file.locations)):
                file.locations[j] = freeSpace.locations[j]
            freeSpace.locations = freeSpace.locations[len(file.locations):]
            break
print(sum(fil.checksum_value() for fil in files))
