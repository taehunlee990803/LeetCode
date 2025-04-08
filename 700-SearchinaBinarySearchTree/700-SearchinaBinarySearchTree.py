#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional
[TreeNode]:
        # if not root:
        #     return []
        # while root:
        #     if root.val > val:
        if not root:
            return []
        while root:
                
            elif root.val > val:
                root = root.left
            if root.val == val:
                return root
            else:
                root = root.right 
        return None
