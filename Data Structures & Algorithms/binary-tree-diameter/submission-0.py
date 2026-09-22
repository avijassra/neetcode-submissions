# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dp(node, diameter):
            nonlocal maxDiameter

            if not node:
                return 0

            leftEdgeCount, rightEdgeCount = 0, 0

            if node.left:
                leftEdgeCount = dp(node.left, diameter) + 1
            
            if node.right:
                rightEdgeCount = dp(node.right, diameter) + 1

            maxDiameter = max(maxDiameter, leftEdgeCount + rightEdgeCount)

            return max(leftEdgeCount, rightEdgeCount)

        dp(root, 0)

        return maxDiameter

            
        