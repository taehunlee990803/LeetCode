        queue = deque([root])
        ans = []
        if not root:
        while queue:
            return ans
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
            current = []
                    queue.append(node.left)
                current.append(node.val)
                if node.right:
                    queue.append(node.right)
            ans.append(current)
        return ans 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
