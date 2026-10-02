# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def buildArray(node):
            if not node:
                return res

            return buildArray(node.left) + [node.val] + buildArray(node.right)


        return buildArray(root)[k-1]
        