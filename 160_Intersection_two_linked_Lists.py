# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if(headA is None or headB is None): return None
        temp1,temp2 = headA,headB
        count1,count2 = 1,1
        while(temp1.next):
            temp1 = temp1.next
            count1 = count1 + 1
        while(temp2.next):
            temp2 = temp2.next
            count2 = count2 + 1
        if(temp1 != temp2): return None

        while(count2>count1):
            headB = headB.next
            count2 = count2-1
        while(count1>count2):
            headA = headA.next
            count1 = count1-1
        
        while(headA and headB):
            if(headA==headB): return headA
            headA = headA.next
            headB = headB.next
        
        return None
        

        