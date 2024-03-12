# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        container = []
        while head:
            container.append(head.val)
            head = head.next
        ans = 0
        temp = 0
        for i in range(len(container)-1,-1,-1):
            if container[i] == 1:
                ans += pow(2,temp)
            temp+=1
        return ans 
[
