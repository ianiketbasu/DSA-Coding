# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0 : return head
        curr = head
        len = 1
        
        while curr.next :
            len+=1
            curr = curr.next
        k %= len
        curr.next = head
        cnt = len - k - 1
        temp = head
        while cnt :
            temp = temp.next
            cnt -= 1
        newHead = temp.next
        temp.next = None
        return newHead