class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        graph = { i:[] for i in range(n) }

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                stack = [i]

                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        stack.extend([nn for nn in graph[node] if nn != node])

                count += 1

        return count