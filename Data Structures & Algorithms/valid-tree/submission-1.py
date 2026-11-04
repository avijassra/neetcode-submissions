from collections import heapq

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return False

        visited = set()
        graph = { i: [] for i in range(n) }
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node, prev):
            if node in visited: return False

            visited.add(node)
            for nn in graph[node]:
                if nn != prev: 
                    if not dfs(nn, node): return False

            return True

        return dfs(0, -1) and len(visited) == n
             
