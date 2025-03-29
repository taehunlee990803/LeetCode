            slow.next = prev
        prev = None

        while slow:
            tmpPointer = slow.next

            slow = slow.next
            prev = slow
            slow = tmpPointer
        
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

