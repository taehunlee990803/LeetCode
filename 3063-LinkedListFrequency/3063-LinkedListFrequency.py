# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = collections.Counter()

        new_head = ListNode(-1, head)
        current = new_head

        while current.next is not None:
            f[current.next.val] += 1
            current = current.next

        return_head = ListNode(-1)
        return_tail = return_head

        for v in f.values():
            return_tail.next = ListNode(v)
            return_tail = return_tail.next
        return return_head.next


[
