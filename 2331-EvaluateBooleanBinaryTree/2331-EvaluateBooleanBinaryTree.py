            elif root.val == 2:
                return self.helper(root.left) or self.helper(root.right)
            elif root.val == 3:
                return self.helper(root.left) and self.helper(root.right)
            else:
                return False
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
            if root.val == 0 or root.val == 1:
                return root.val == 1
class Solution:
    def helper(self, root):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


        if root is None:
[
