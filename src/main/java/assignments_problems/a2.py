def maxSubArray(nums):
    currentSum = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):
        currentSum = max(nums[i], currentSum + nums[i])

        if currentSum > maxSum:
            maxSum = currentSum

    return maxSum


nums = list(map(int, input("Enter numbers: ").split()))

print(maxSubArray(nums))