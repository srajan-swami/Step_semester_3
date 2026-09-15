def maxProfit(prices):
    lowestPrice = prices[0]
    maxProfitValue = 0

    for price in prices:
        if price < lowestPrice:
            lowestPrice = price

        profit = price - lowestPrice

        if profit > maxProfitValue:
            maxProfitValue = profit

    return maxProfitValue


prices = list(map(int, input("Enter prices: ").split()))

print(maxProfit(prices))