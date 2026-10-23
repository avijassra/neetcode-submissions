class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, maxCap, maxHeight  = 0, len(heights)-1, 0, max(heights)

        while l < r:
            height = min(heights[l], heights[r])
            cap = height * (r-l)
            maxCap = max(maxCap, cap)

            if height == heights[l]:
                l += 1

            if height == heights[r]:
                r -= 1

            if maxHeight * (r-l) < cap:
                break

        return maxCap
            