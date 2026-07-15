class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count = 1
        profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(len(prices)):
                print(j)
                sell = prices[j]
                diff = sell - buy
                if j>i and diff > profit:
                    profit = diff
        return profit

