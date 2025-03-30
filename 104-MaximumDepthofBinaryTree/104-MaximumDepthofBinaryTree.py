        level = 0

        while queue:
            level += 1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
        if not root:
            return 0
