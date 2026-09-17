/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists) {
        let resultList = null;
        for(let i = 0; i < lists.length; i++) {
            resultList = this.merge2Lists(resultList, lists[i]);
        }

        return resultList;
    }

    merge2Lists(l1, l2) {
        if(l1 === null) return l2;
        if(l2 === null) return l1;

        if(l1.val < l2.val) {
            l1.next = this.merge2Lists(l1.next, l2);
            return l1;
        } else {
            l2.next = this.merge2Lists(l1, l2.next);
            return l2;
        }
    }
}
