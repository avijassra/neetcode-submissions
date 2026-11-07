class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp =[0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            if len(stack) > 0:
                while len(stack) > 0 and t > stack[-1][0]:
                    t1, i1 = stack.pop()
                    dp[i1] = i - i1

            stack.append((t, i))

        return dp
