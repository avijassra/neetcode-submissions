class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()
        checked.add(n)

        while n != 1:
            new_sum = 0
            while n != 0:
                n, new_n = divmod(n, 10)
                new_sum += (new_n**2)
            n = new_sum

            if n in checked:
                return False
            else:
                checked.add(n)

        return True