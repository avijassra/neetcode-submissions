class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0: return False

        counter = Counter(hand)

        for k in sorted(counter):
            c = counter[k]

            if c == 0:
                continue

            for i in range(groupSize):
                if k+i not in counter or counter[k+i] < c:
                    return False

                counter[k+i] -= c

        return True