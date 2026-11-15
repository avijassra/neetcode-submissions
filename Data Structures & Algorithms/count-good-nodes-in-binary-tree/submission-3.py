from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        if not root: return good

        q = deque([(root, root.val)])

        while q:
            node, max_so_far = q.popleft()

            if node.val >= max_so_far: good += 1
            max_so_far = max(node.val, max_so_far)

            if node.left: q.append((node.left, max_so_far))
            if node.right: q.append((node.right, max_so_far))

        return good