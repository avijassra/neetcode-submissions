"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = copy = Node(-1)
        headDup = head
        nodes = {}

        while headDup:
            copy.next = Node(headDup.val)
            nodes[headDup] = copy.next
            copy, headDup = copy.next, headDup.next

        copy, headDup = res.next, head
        while headDup:
            if headDup.random: 
                copy.random = nodes[headDup.random]
            copy, headDup = copy.next, headDup.next

        return res.next