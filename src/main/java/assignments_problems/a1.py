def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    leftProduct = 1

    for i in range(n):
        answer[i] = leftProduct
        leftProduct *= nums[i]

    rightProduct = 1

    for i in range(n - 1, -1, -1):
        answer[i] *= rightProduct
        rightProduct *= nums[i]

    return answer


nums = list(map(int, input("Enter numbers: ").split()))

print(productExceptSelf(nums))