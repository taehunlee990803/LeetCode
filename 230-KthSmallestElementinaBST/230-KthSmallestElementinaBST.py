# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            nodes.append(current.val)
            current = current.right

        return nodes[k-1]
