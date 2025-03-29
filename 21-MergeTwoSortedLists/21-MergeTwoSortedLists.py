        current = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
            else:
                current.next = list1
                list1 = list1.next
                current.next = list2
                list2 = list2.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy.next
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
                current = current.next
                current = current.next

