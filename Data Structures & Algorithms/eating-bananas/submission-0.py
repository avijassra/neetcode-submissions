class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_at(rate: int) -> int:
            return sum((p + rate - 1) // rate for p in piles)  # ceil(p / rate)

        l, r = 1, max(piles)

        while l < r:
            m = (r + l) // 2

            if hours_at(m) <= h:
                r = m
            else:
                l = m + 1

        return l