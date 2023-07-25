# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None 
        
        current = head
        prev = None
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev
            
        
        
        
#         count =0 
#         temp = head
#         new_arr = []
#         while temp.next != None:
#             new_arr.append(temp.val)
#             temp = temp.next
#             count+=1
            
#         while head.next != None:
#             element = new_arr[count-1]
#             head.val = element
#             new_arr.remove(element)
#         return head
        