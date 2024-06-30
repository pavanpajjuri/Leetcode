# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        carry = 0

        while(l1 and l2):
            val = l1.val+l2.val+carry
            if val >= 10:
                carry = 1
                val = val-10
            else:
                carry = 0
            l1,l2 = l1.next,l2.next
            curr.next = ListNode(val)
            curr = curr.next

        while(l1):
            val = l1.val+carry
            if val >= 10:
                carry = 1
                val = val-10
            else:
                carry = 0

            l1 = l1.next
            curr.next = ListNode(val)
            curr = curr.next
        while(l2):
            val = l2.val+carry
            if val >= 10:
                carry = 1
                val = val-10
            else:
                carry = 0
                
            l2 = l2.next
            curr.next = ListNode(val)
            curr = curr.next
            
        if(carry):
            curr.next = ListNode(1)

        return head.next

        