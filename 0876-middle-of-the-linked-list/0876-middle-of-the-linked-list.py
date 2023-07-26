# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer = head
        count = 0
        temp = 1
        
        while pointer:
            pointer = pointer.next
            count+=1
            

        count = int(count/2)+1
        while temp != count:
            head = head.next
            temp+=1
   
        return head
            