class Solution:
    def countBits(self, n: int) -> List[int]:
        output, base = [0], 1
        for i in range(1, n+1):
            if i == 2*(base):
                base = i
            
            output.append(output[i-base]+1)
            
        return output