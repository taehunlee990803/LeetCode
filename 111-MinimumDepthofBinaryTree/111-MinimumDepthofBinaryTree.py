            #     if node.right:
            #         queue.append(node.right)
            #     if not node.left and not node.right:
            #         # min_ans = min(min_ans, current)
            #         return level
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level+1))
            #         queue.append(node.left)
            #     if node.left:
            #     node = queue.popleft()
            # for i in range(len(queue)):
            # level += 1
        while queue:
        # min_ans = current
        queue = deque([(root, 1)])
