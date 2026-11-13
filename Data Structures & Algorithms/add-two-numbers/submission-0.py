# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(listNode) -> int:
            place = 1
            number = 0

            while listNode:
                number += (place * listNode.val)
                place *= 10
                listNode = listNode.next

            return number

        n1 = getNum(l1)
        n2 = getNum(l2)
        n3 = n1 + n2

        if n3 == 0: return ListNode(0)

        res = node = ListNode()
        while n3 > 0:
            n3, q = divmod(n3, 10)
            node.next = ListNode(q)
            node = node.next
            
        return res.next
        