        before.next = after_x.next
        after.next = None


        return before_x.next


        after_x = ListNode(0)

        before = before_x
        after = after_x

        current = head

        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after= after.next
            current = current.next


        before_x = ListNode(0)
        
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
[
