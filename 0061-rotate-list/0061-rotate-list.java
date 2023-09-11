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
    public ListNode rotateRight(ListNode head, int k) {
        
        if(head == null || head.next == null || k == 0) return head;
        
        ListNode dummy = head;
        int len = 1;
        while(dummy.next != null){
            len++;
            dummy = dummy.next;
        }
        
        dummy.next = head;
        k = len - (k % len) - 1;
        
        while(k > 0){
            head = head.next;
            k--;
        }
        
        dummy = head.next;
        head.next = null;
        
        return dummy;
    }
}