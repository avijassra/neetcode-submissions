class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            l_r_sum = numbers[l] + numbers[r]
            if l_r_sum == target:
                return [l+1, r+1]
            elif l_r_sum > target:
                r -= 1
            else:
                l += 1
            
        return []



        