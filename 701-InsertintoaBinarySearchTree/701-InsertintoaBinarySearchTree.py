# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while True:
        new_node = TreeNode(val)

        if not root:
            return new_node
        current = root
            if current.val < val:
            elif current.val > val:

                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    break
        return root 
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    break


