    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        rightsubtree  = root.right
        leftsubtree = root.left
        
        root.left = None

        self.flatten(leftsubtree)
        root.right = leftsubtree

        current = root
        while current.right:
            current = current.right
        
        self.flatten(rightsubtree)
        current.right =rightsubtree
        
