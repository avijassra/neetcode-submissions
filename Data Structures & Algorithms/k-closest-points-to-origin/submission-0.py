import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        heapq.heapify(arr)

        for x, y in points:
            d = -((x)**2 + (y)**2)
            heapq.heappush(arr, (d, x, y))

            if len(arr) > k:
                heapq.heappop(arr)

        return [[x, y] for _, x, y in arr]
