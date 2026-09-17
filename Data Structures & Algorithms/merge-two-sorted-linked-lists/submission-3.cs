/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null) {
            return list2;
        }

        if(list2 == null) {
            return list1;
        }

        var currL1 = list1;    
        var currL2 = list2;
        ListNode list = (currL1.val < currL2.val) ? currL1 : currL2;
        var resp = list;

        if(currL1.val < currL2.val) {
            currL1 = currL1.next;
        } else {
            currL2 = currL2.next;
        }

        while (currL1 != null && currL2 != null) {
            if(currL1.val < currL2.val) {
                list.next = currL1;
                currL1 = currL1.next;
            } else {
                list.next = currL2;
                currL2 = currL2.next;
            }

            list = list.next;
        }

        if(currL1 == null) {
            list.next = currL2;
        } else {
            list.next = currL1;
        }

        return resp;
        
    }
}