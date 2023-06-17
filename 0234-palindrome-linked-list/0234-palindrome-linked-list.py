# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         s = ""
#         while head :
#             s += str(head.val)
#             head = head.next
        
#         return s == s[::-1]

        prev = None
        slow = fast = head
        
        while fast and fast.next :
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        if fast :
            slow = slow.next
        
        while prev :
            if slow.val != prev.val :
                return False
            prev , slow = prev.next , slow.next
        
        return True