        dummy_head = ListNode()
        dummy_head.next = head 

        current_node = dummy_head

        while current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return dummy_head.next 






