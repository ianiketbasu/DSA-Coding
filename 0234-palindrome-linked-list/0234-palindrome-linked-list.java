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

import java.util.*;
class Solution {
    public boolean isPalindrome(ListNode head) {
        String s = "";
        while(head != null){
            s += (char)(head.val + '0');
            head = head.next;
        }
        int i = 0 , j = s.length()-1;
        while(i <= j){
            if(s.charAt(i++)!=s.charAt(j--)){
                return false;
            }
        }
        return true;
    }
}