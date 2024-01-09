# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node and not node.left and not node.right

        left_sum = 0

        if root is None:
            return 0

         # Check if the left child is a leaf and add its value
        if root.left and isLeaf(root.left):
            left_sum += root.left.val

        # Recursively calculate the sum for left and right subtrees
        left_sum += self.sumOfLeftLeaves(root.left)
        left_sum += self.sumOfLeftLeaves(root.right)

        return left_sum
[3,9,20,null,null,15,7]
