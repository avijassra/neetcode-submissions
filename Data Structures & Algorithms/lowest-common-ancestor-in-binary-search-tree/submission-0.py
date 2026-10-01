# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lower = p.val if p.val < q.val else q.val
        higher = q.val if q.val > p.val else p.val

        def searchlca(node):
            if not node:
                return None

            if (lower < node.val < higher) or (lower == node.val and higher > node.val) or (lower < node.val and higher == node.val):
                return node

            if lower < node.val and higher < node.val:
                return searchlca(node.left)

            if lower > node.val and higher > node.val:
                return searchlca(node.right)

            return None

        return searchlca(root)