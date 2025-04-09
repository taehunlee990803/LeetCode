        currentLevel = 0
        maxLevel = 1
        stack = deque([root])

        while stack:
            qLen = len(stack)
            tempSum = 0
                node = stack.popleft()
                if node:
                    tempSum += node.val
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            currentLevel += 1
            if tempSum > maxSum:
                maxLevel = currentLevel
                maxSum = tempSum
        return maxLevel
        maxSum= root.val
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
                print(tempSum, currentLevel)
            for i in range(qLen):

            print(qLen)
