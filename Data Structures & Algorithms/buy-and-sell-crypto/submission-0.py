class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buyAt, sellAt, profit = prices[0], prices[0], 0

        for i in range(1, len(prices)):
            if prices[i-1] > prices[i]:
                buyAt = prices[i] if buyAt > prices[i] else buyAt
                sellAt = prices[i-1]
            elif prices[i-1] < prices[i]:
                sellAt = prices[i]
                profit = max(sellAt-buyAt, profit)

        return profit

        