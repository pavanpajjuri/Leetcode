# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(head is None or left==right): return head
        prev = dummy = ListNode(None)
        prev.next = head
        for _ in range(left-1):
            prev = prev.next

        curr = prev.next

        for _ in range(right-left):
            temp = prev.next
            prev.next = curr.next
            curr.next = prev.next.next
            prev.next.next = temp
        
        return dummy.next
        

        