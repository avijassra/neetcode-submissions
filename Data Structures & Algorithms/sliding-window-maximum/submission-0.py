from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for i, n in enumerate(nums):
            while len(q) > 0 and n > q[-1][0]:
                q.pop()

            q.append((n, i))

            if q[0][1] <= i-k:
                q.popleft()

            if i >= k-1:
                res.append(q[0][0])

        return res