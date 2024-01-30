class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return ans
        return preOrder(root,ans)
        def preOrder(root, ans):
            ans.append(root.val)
            preOrder(root.left, ans)
            preOrder(root.right, ans)
            return ans 
        ans = []

    
[
