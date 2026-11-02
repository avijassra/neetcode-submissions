class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n, res = 0, len(intervals), []
        start, end = newInterval
        
        while i < n and start > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        while i < n and end >= intervals[i][0]:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        
        res.append([start, end])
        res.extend(intervals[i:])

        return res