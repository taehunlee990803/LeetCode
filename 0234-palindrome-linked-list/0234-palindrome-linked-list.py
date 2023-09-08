# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        new_arr = []
        current_node = head
        while current_node is not None:
            new_arr.append(current_node.val)
            current_node = current_node.next
        
        end = len(new_arr)
        for i in range(0,len(new_arr)):
            if new_arr[i] != new_arr[end-1]:
                return False
            end -=1 
        return True