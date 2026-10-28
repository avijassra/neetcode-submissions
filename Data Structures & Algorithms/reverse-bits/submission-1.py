Table = []
for b in range(256):
    r = 0
    for _ in range(8):
        r = (r << 1) | (b & 1)
        b >>= 1
    Table.append(r)

class Solution:
    def reverseBits(self, n: int) -> int:
        A = (n >> 24) & 0xFF
        B = (n >> 16) & 0xFF
        C = (n >> 8) & 0xFF
        D = n & 0xFF

        return (Table[D] << 24) | (Table[C] << 16) | (Table[B] << 8) | Table[A]