class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, maxProfit  = float('inf'), None, 0

        for p in prices:
            if p < buy:
                buy, sell = p, None

            if not sell or p > sell:
                sell = p

            if sell:
                maxProfit = max(maxProfit, sell-buy)

        return maxProfit