class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = {}
        preMap = {i:deque([]) for i in range(numCourses) }
        visited = set()

        for c, p in prerequisites:
            preMap[c].append(p)

        def dfs(c):
            if c not in visited:
                visited.add(c)

                while len(preMap[c]) > 0:
                    if not dfs(preMap[c][0]):
                        return False

                    p = preMap[c].popleft()

                    if p not in res:
                        res[p] = 1

                if c not in res:
                    res[c] = 1
                    
            return len(preMap[c]) == 0
            
        if all(dfs(i) for i in range(numCourses)):
            return list(res.keys())
        else:
            return []