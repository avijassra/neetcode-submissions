class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i, n = 1, len(intervals)
        output = []
        prevStart, prevEnd = intervals[0]

        for start, end in intervals[1:]:
            if prevEnd < start:
                output.append([prevStart, prevEnd])
                prevStart, prevEnd = start, end
            elif start <= prevEnd <= end:
                prevEnd = end

        output.append([prevStart, prevEnd])

        return output