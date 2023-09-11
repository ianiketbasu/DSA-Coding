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
    public ListNode middleNode(ListNode head) {
        ListNode dummy = head;
        int len = 0;
        
        while(dummy != null){
            len++;
            dummy = dummy.next;
        }
        
        ListNode middle = head;
        len = (len / 2) + 1;
        while(len > 1){
            middle = middle.next;
            len--;
        }
        
        return middle;
    }
}