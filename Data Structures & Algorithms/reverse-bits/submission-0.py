class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # 1. Shift result left to make room for the next bit
            result <<= 1
            # 2. Extract the last bit of num and add it to result
            result |= (n & 1)
            # 3. Shift num right to process the next bit
            n >>= 1
        return result
        