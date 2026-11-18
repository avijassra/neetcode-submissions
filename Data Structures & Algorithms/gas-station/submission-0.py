class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        in_tank = 0
        start_idx = -1

        for idx, (g, c) in enumerate(zip(gas, cost)):
            if g - c + in_tank >= 0:
                in_tank = g - c + in_tank
                if start_idx < 0:
                    start_idx = idx
            else:
                start_idx = -1
                in_tank = 0

        return start_idx