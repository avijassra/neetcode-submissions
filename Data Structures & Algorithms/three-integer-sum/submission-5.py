class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nLen = len(nums)
        nums.sort()

        for i in range(nLen-2):
            l, r = i + 1, nLen - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    if (nums[i], nums[l], nums[r]) not in res:
                        res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return list(res)