        prev = None
        for i in range(right - left + 1): # 4 - 2 + 1 = 3
            tmpNext = current.next
            current.next = prev
            prev = current
            current = tmpNext

        leftPrev.next.next = current 
        leftPrev.next = prev

        return dummy_node.next
