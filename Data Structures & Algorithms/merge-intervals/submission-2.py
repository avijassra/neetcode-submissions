class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # print(f'{intervals[-1][1]} < {start}')
            if output[-1][1] < start:
                output.append([start, end])
            elif end > output[-1][1]:
                output[-1][1] = end

            # print(output)

        return output