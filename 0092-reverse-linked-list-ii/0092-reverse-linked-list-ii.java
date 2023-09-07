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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(left == right) return head;
        
        ListNode prev = null , curr = head;
        
        while(left > 1){
            left--;
            prev = curr;
            curr = curr.next;
            right--;
        }
        
        ListNode start = prev , tail = curr , temp = null;
        
        while(right > 0){
            temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
            right--;
        }
        
        if(start != null) start.next = prev;
        else head = prev;
        
        tail.next = curr;

        return head;
    }
}