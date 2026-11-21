from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.points_on_x = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x,y)] += 1
        self.points_on_x[x].add(y)

    def count(self, point: List[int]) -> int:
        x, y = point
        cnt = self.points
        sq_count = 0

        for dy in self.points_on_x[x]:
            d = y - dy

            for dx in [d, -d]:
                if y == dy: continue

                sq_count += (cnt[(x, dy)] * cnt[(x+dx, y)] * cnt[(x+dx, dy)])

        return sq_count
        
