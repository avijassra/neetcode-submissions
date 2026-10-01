# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        def bfs(node, ind):
            if node:
                if len(res) < ind + 1:
                    res.append([])

                res[ind].append(node.val)

                if node.left:
                    bfs(node.left, ind + 1)

                
                if node.right:
                    bfs(node.right, ind + 1)

        bfs(root, 0)

        return res