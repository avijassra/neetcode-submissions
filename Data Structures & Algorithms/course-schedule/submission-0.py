class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:deque([]) for i in range(numCourses)}
        visited = set()

        for c,p in prerequisites:
            preMap[c].append(p)
        
        def dfs(c):
            if c not in visited:
                visited.add(c)
                
                while len(preMap[c]) > 0:
                    if not dfs(preMap[c][0]):
                        return False

                    preMap[c].popleft()
                    
            return len(preMap[c]) == 0

        return all(dfs(i) for i in range(numCourses))