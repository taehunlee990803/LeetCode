# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        def traverse(root,ans):
            if root:
               traverse(root.left, ans)
               ans.append(root.val)
       
               traverse(root.right, ans)
        traverse(root, ans)
        for element in ans:
        sum_value = 0
            if element >= low and element <= high:
                sum_value += element
        return sum_value
[10,5,15,3,7,null,18]
