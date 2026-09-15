def rotateArray(nums, k):
    n = len(nums)

    if n == 0:
        return nums

    k = k % n

    newArray = [0] * n

    for i in range(n):
        newPosition = (i + k) % n
        newArray[newPosition] = nums[i]

    return newArray


nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

print(rotateArray(nums, k))
