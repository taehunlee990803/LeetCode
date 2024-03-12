# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        hashmap = defaultdict(int)
        while head:
            hashmap[head.val] += 1
            head = head.next

        rst_head = ListNode()
        rst = rst_head
        for a,b in hashmap.items():
            rst.next = ListNode(val = b)
            rst = rst.next
        return rst_head.next
[
