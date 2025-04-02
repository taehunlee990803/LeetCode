        nodes = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            nodes.append(current.val)
            current = current.right
        # print(nodes)
        n = len(nodes)
        mid = n // 2
        root = TreeNode(nodes[mid])

        q = deque()
        q.append((root, 0, mid-1))
        q.append((root, mid+1, n -1 ))

        while q:
            parent, left, right = q.popleft()
            if left <= right:
                mid = (left + right) // 2
                child = TreeNode(nodes[mid])
                if nodes[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child 
                q.append((child, left, mid-1))
                q.append((child, mid + 1, right ))
        return root
