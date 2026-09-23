# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return (True, 0)

            leftBal, left = dfs(node.left)
            rightBal, right = dfs(node.right)

            return (leftBal and rightBal and abs(left-right) <= 1, max(left, right) + 1)
        
        lb, l = dfs(root.left)
        rb, r = dfs(root.right)

        return lb and rb and abs(l-r) <= 1