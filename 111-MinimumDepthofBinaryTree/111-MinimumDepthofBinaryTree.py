            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    # min_ans = min(min_ans, current)
            level += 1
                    return level
            # current += 1
        # return min_ans

        
