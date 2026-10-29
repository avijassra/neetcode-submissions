# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        b, s = p.val if p.val > q.val else q.val, q.val if p.val > q.val else p.val

        if s <= root.val <= b:
            return root

        if root.val > b:
            return self.lowestCommonAncestor(root.left, p, q)

        
        if root.val < s:
            return self.lowestCommonAncestor(root.right, p, q)

        return None
