from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        visited = {}
        q = deque([node])
        visited[node] = Node(node.val, [])

        while q:
            n = q.popleft()
            
            for nn in n.neighbors:
                if nn not in visited:
                    q.append(nn)
                    visited[nn] = Node(nn.val, [])

                visited[n].neighbors.append(visited[nn])

        return visited[node]

        



        