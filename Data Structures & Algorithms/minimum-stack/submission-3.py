import heapq

class MinStack:

    def __init__(self):
        self.nums = []
        

    def push(self, val: int) -> None:
        if len(self.nums) == 0:
            self.nums.append((val, val))
        else:
            _, minVal = self.nums[-1]
            minVal = min(minVal, val)

            self.nums.append((val, minVal))

    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        val, _ = self.nums[-1]
        return val

    def getMin(self) -> int:
        _, minVal = self.nums[-1]
        return minVal