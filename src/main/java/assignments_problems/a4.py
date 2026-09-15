def subarraySum(nums, k):
    prefixSum = 0
    count = 0
    frequency = {0: 1}

    for num in nums:
        prefixSum += num

        requiredSum = prefixSum - k

        if requiredSum in frequency:
            count += frequency[requiredSum]

        if prefixSum in frequency:
            frequency[prefixSum] += 1
        else:
            frequency[prefixSum] = 1

    return count


nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

print(subarraySum(nums, k))