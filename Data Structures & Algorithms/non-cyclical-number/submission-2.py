class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            tempSum = 0
            newN = n
            while newN != 0:
                newN, r = divmod(newN, 10)
                tempSum += r**2

            n = tempSum
            if n not in seen:
                seen.add(n)
            else:
                break
                
        return True if n == 1 else False