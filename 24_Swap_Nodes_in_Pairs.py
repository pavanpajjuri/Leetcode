# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None): return head

        prev = ListNode()
        curr = head
        ans = head.next

        while(curr and curr.next):
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr

            prev = curr
            curr = curr.next
        
        return ans

        