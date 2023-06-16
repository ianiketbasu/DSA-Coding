# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(-1)
        newHead.next = head
        slow = fast = newHead

        while n:
            fast = fast.next
            n -= 1
        
        while fast.next:
            slow, fast = slow.next, fast.next

        temp = slow.next
        slow.next = slow.next.next
        temp.next = None
        del temp

        return newHead.next

        
        