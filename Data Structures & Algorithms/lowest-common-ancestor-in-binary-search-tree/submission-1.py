# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lower, higher = min(p.val, q.val), max(p.val, q.val)

        def searchlca(node):
            if not node:
                return None

            if (lower <= node.val <= higher):
                return node

            if higher < node.val:
                return searchlca(node.left)

            if lower > node.val:
                return searchlca(node.right)

        return searchlca(root)