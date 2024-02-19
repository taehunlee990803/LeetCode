#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        
            
        while pA != pB:
            pB = pB.next if pB else headA
        return pA
            pA = pA.next if pA else headB
#         self.val = x
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
8
