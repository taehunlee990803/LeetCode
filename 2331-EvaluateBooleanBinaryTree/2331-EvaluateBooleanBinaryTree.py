                else:
                    return False
            elif root.val == 2:
                return self.helper(root.left) or self.helper(root.right)
            elif root.val == 3:
                return self.helper(root.left) and self.helper(root.right)
            else:
                return False
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:


        if root is None:
            return False

        return self.helper(root)
[
