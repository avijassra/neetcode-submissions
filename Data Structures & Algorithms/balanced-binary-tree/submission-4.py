# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)

            lb, lh = dfs(node.left)
            rb, rh = dfs(node.right)

            if (not lb or not rb):
                return (False, 0)

            return (abs(lh-rh) <= 1, max(lh, rh) + 1)
            
        return dfs(root)[0]