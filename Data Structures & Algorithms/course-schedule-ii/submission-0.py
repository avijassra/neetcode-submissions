class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap = { i:deque([]) for i in range(numCourses)}
        visited = set()
        orderedDict = {}

        for c,p in prerequisites:
            preMap[c].append(p)
        
        def dfs(c):
            if c not in visited:
                visited.add(c)
                
                while len(preMap[c]) > 0:
                    if not dfs(preMap[c][0]):
                        return False

                    p = preMap[c].popleft()
                    if p not in orderedDict:
                        orderedDict[p] = 1

                if c not in orderedDict:
                    orderedDict[c] = 1

            return len(preMap[c]) == 0

        if all(dfs(i) for i in range(numCourses)):
            return list(orderedDict.keys())
        else:
            return []