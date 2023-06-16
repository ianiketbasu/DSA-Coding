# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0)
        temp = newHead
        carry = 0
        while l1 and l2 :
            sumVal = l1.val + l2.val + carry
            
            temp.next = ListNode((sumVal%10))
            carry = sumVal // 10
            temp = temp.next
            l1 , l2 = l1.next , l2.next

        remaining = l1 or l2
        while remaining:
            sumVal = remaining.val + carry
            carry = sumVal // 10
            temp.next = ListNode(sumVal % 10)
            temp = temp.next
            remaining = remaining.next
        
        if carry :
            temp.next = ListNode(carry)
        
        return newHead.next
        
            