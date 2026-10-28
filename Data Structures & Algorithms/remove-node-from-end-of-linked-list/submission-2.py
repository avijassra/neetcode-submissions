# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listNodeLen = 0
        res = ListNode()
        output = res

        curr = head
        while curr:
            listNodeLen += 1
            curr = curr.next

        print(f'1. {listNodeLen}')

        removeAtInd = listNodeLen - n + 1
        print(f'2. {removeAtInd}')
        ind, curr = 0, head
        while curr:
            ind += 1
            if ind != removeAtInd:
                print(f'{ind} != {removeAtInd}:')
                output.next= ListNode(curr.val)
                output = output.next
            
            curr = curr.next

        return res.next