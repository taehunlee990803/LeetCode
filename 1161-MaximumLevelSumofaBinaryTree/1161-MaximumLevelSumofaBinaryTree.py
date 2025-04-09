        currentLevel = 0
        maxLevel = 1
        stack = deque([root])

        while stack:
            qLen = len(stack)
                node = stack.popleft()
                if node:
                    tempSum += node.val
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            currentLevel += 1
            if tempSum > maxSum:
                maxSum = tempSum
        return maxLevel
        maxSum= root.val
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
                maxLevel = currentLevel
            for i in range(qLen):

            tempSum = 0
                    
