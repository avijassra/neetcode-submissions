class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        minHeight = min(height[l], height[r])

        while l < r:
            if height[l] <= minHeight:
                area += minHeight - height[l]
                height[l] = minHeight
                l += 1
            elif height[r] <= minHeight:
                area += minHeight - height[r]
                height[r] = minHeight
                r -= 1
            else:
                minHeight = min(height[l], height[r]) 
            
        return area     