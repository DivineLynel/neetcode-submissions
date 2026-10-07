class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        max_profit = 0
        for i in range(len(prices)):
            right = i

            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

        return max_profit