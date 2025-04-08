



        return level
                    queue.append(node.right)
                if node.right:
                if node.left:
                    queue.append(node.left)
                node = queue.popleft()

            level += 1
            for i in range(len(queue)):

        while queue:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0

