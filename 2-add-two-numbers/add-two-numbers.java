/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        int val1 = 0;
        int val2 = 0;
        ListNode result = null;
        ListNode temp = null;
        while(l1 != null  || l2 != null || carry != 0){
            val1 = l1 != null ? l1.val : 0;
            val2 = l2 != null ? l2.val : 0;
            if(result == null){
                result = new ListNode((val1 + val2)%10);
                carry = (val1 + val2)/10;
                temp = result;
            } else{
                result.next = new ListNode((val1 + val2 + carry)%10);
                carry = (val1 + val2 + carry)/10;
                result = result.next;
            }
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }
        return temp;
    }
}