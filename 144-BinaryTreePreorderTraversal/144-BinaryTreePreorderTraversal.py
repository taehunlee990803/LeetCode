#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postOrder(root, ans):
            if root is None:
                return ans
            postOrder(root.left, ans)
            postOrder(root.right, ans)
            ans.append(root.val)
        return postOrder(root, ans)
        ans = []
            return ans 

[
