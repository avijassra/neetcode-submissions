from collections import defaultdict
from functools import cache 

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        from_to = defaultdict(list)
        
        for f, t, c in flights:
            from_to[f].append((t, c))

        @cache
        def dp(s, r):
            # do something
            if s == dst: return 0
            if r == 0: return float('inf')

            return min((c + dp(v, r-1) for v, c in from_to[s]), default=float('inf'))

        ans = dp(src, k + 1)
        return -1 if ans == float('inf') else ans