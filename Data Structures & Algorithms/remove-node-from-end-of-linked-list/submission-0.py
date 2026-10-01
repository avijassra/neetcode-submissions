# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: return head

        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n+1):
            fast = fast.next

        # Move both until fast falls off the end
        while fast:
            fast = fast.next
            slow = slow.next

        # slow is now right before the node to remove
        slow.next = slow.next.next

        return dummy.next        