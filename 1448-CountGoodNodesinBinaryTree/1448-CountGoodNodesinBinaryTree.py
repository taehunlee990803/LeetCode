

        return dfs(root, root.val)

                res = 0

            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            if node.val >= maxVal:
                res = 1
            else:
        def dfs(node, maxVal):
            if not node:
                return 0
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int: 
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
            return res 
