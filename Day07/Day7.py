with open('Input.txt', 'r') as f:
    data = f.read().split('\n')


def split_or_sub(res: int, nums: list, isPart2: bool = False):
    if len(nums) == 1:
        if res == nums[0]:
            return True
        return False
    currentNumber = nums[0]
    if res % currentNumber == 0:
        if split_or_sub(res // currentNumber, nums[1:], isPart2):
            return True
    if res - currentNumber > 0 and split_or_sub(res - currentNumber, nums[1:], isPart2):
        return True
    if isPart2 and str(res).endswith(str(currentNumber)) and res != currentNumber:
        if split_or_sub(int(str(res)[:-len(str(currentNumber))]), nums[1:], isPart2):
            return True
    return False


totalCalibrationResult1 = 0
totalCalibrationResult2 = 0
for i, row in enumerate(data):
    result, numbers = row.split(':')
    result = int(result)
    numbers = [int(num) for num in numbers.strip().split(' ')][::-1]
    # Part1
    if split_or_sub(result, numbers):
        totalCalibrationResult1 += result
    # Part2
    if split_or_sub(result, numbers, True):
        totalCalibrationResult2 += result
print(totalCalibrationResult1)
print(totalCalibrationResult2)



