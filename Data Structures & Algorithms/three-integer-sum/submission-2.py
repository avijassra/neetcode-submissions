class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_n = len(nums)
        nums.sort()

        res = []

        for i in range(len_n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len_n - 1

            while l < r:
                i_l_r_sum = nums[i] + nums[l] + nums[r]
                if  i_l_r_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif i_l_r_sum > 0:
                    r -= 1
                else:
                    l += 1
            
        return res