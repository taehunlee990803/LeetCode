        # while current:

        # prev = None
        # current = head
        #     return None

        # if not head:
            prev = current
            current = next_node
            current.next = prev
            next_node = current.next

        while current:
        prev = None
        current = head

        if not head:
            return None
:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]
class Solution:
        return prev
