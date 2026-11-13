# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = node = ListNode()
        carryFwd = 0

        while l1 or l2 or carryFwd:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            num = carryFwd + l1Val + l2Val

            if num > 9:
                carryFwd, num = divmod(num, 10)
            else:
                carryFwd = 0

            node.next = ListNode(num)
            node, l1, l2 = node.next, l1.next if l1 else None, l2.next if l2 else None

        return res.next