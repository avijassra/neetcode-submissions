class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1: return False

        tracker = []

        for b in s:
            if b == '(':
                tracker.append(')')
            elif b == '{':
                tracker.append('}')
            elif b == '[':
                tracker.append(']')
            elif len(tracker) > 0 and b == tracker[-1]:
                tracker.pop(-1)
            else:
                return False

        return len(tracker) == 0
