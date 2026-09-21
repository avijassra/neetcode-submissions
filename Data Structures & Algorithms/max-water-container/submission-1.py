class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        maxHeights = max(heights)

        l, r = 0, len(heights) - 1

        while l < r:
            cont_height = min(heights[l], heights[r])
            cont_area = cont_height * (r - l)
            area = max(cont_area, area)

            if heights[l] == cont_height:
                l += 1

            if heights[r] == cont_height:
                r -= 1

            if maxHeights * (r-l) < area:
                break

        return area
