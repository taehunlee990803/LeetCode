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
        print(count)
        if count%2 == 0:
            count = int(count/2)+1
            print("even",count)
            while temp != count:
                head = head.next
                temp+=1
        else:
            count = int(count/2)+1
            print("odd",count)
  
            while temp != count:
                head = head.next
                temp+=1
        print(temp)
        return head
            