def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        middle = (left + right) // 2

        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle

    return nums[left]


nums = list(map(int, input("Enter numbers: ").split()))

print(findMin(nums))