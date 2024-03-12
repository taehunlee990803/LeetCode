#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        oddPoint = 0
        
        evenPoint = 0
        while head:
            even = head.val
            head = head.next
            odd = head.val
            head = head.next
            if even > odd:
                evenPoint += 1
            else:
                oddPoint += 1
        if evenPoint > oddPoint:
            return "Even"
        elif evenPoint < oddPoint:

            return "Odd"
        else:
            return "Tie"
[
