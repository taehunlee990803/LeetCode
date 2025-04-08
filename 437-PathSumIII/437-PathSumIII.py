#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # if not root:
        #     return 0
        # self.count = 0
        self.total = 0
        def helper(node, cur):
            if not node:
                return
            helper(node.left, cur + node.val)
            helper(node.right, cur + node.val)
            if cur + node.val == targetSum:
                self.total += 1
        def dfs(node):
            if not node:
                return
            helper(node, 0)
            dfs(node.left)
            dfs(node.right)
        return self.total
        dfs(root)
