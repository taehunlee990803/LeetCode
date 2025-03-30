        queue = deque([root])
        result = []

        while queue:
            level = []
            for i in range(len(queue)):

        print(len(queue))
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sum(level)/len(level))
            
        return result         
