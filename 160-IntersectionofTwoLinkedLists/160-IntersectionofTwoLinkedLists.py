# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        containerA = []
        containerB = []
        
        while a:
            containerA.append(a)
            a = a.next
        while b:
            if b in containerA:
                return b
            b = b.next
        #     containerB.append(b.val)
        #     b = b.next
        # print(containerA, containerB)
        # for i in range(len(containerA)):
        #     for j in range(len(containerB)):
        #         if containerA[i] == containerB[j]:
        #             return containerA[i]
        return None
8
