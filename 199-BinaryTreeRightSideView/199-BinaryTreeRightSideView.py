#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque([root])

        while stack:

        ans = []
        # We gotta use BFS method to check the right side node
            for i in range(qLen):
            qLen = len(stack)
            rightSide = None
                node = stack.popleft()
                if node:
                    stack.append(node.left)
                    stack.append(node.right)
                    rightSide = node
            if rightSide:
                ans.append(rightSide.val)
        return ans 
