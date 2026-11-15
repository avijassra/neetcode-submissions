# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def diameter(node):
            nonlocal maxDiameter

            if not node: return 0

            lDia, rDia = diameter(node.left), diameter(node.right)
            currDiameter = lDia + rDia
            maxDiameter = max(maxDiameter, currDiameter)

            return max(lDia, rDia) + 1

        diameter(root)  

        return maxDiameter
