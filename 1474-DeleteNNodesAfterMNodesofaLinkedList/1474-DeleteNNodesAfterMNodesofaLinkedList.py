# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        ans_list = ListNode()
        while head:
            if tempM > 0:
        new_list = ans_list
                new_list.next = ListNode(head.val)
                tempM-=1
                new_list = new_list.next
            if tempM == 0:
                if tempN > 0:
                    tempN-= 1
                elif tempN == 0:
                    tempM = m
        tempM = m
        tempN = n
                    tempN = n
        return ans_list.next 
            head = head.next
[
