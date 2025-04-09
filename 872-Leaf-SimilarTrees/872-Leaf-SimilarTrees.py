        while second:

                if node.right:
                    first.append(node.right)
                    first.append(node.left)
                    left.append(node.val)
                if node.left:
                node = first.pop()
                if not node.left and not node.right:
        while first:
            for i in range(len(first)):
        second = deque([root2])


        first = deque([root1])
        left = []
        right = []
            for i in range(len(second)):
                node = second.pop()
                if not node.left and not node.right:
                    right.append(node.val)
                if node.left:
