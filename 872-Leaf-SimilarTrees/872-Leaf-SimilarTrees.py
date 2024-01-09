
        # Get leaf values for both trees
        leaf_values1 = get_leaf_values(root1)
        leaf_values2 = get_leaf_values(root2)

        # Check if the leaf values are the same
        return leaf_values1 == leaf_values2

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_values(root):
            

        # Helper function for in-order traversal
        def traverse(node, result):
           
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
            result = []
            if root:
                traverse(root, result)
            return result
            if node.left is None and node.right is None:
                result.append(node.val)
            else:
                if node.left:
                    traverse(node.left, result)
                if node.right:
                    traverse(node.right, result)
            
        
[3,5,1,6,2,9,8,null,null,7,4]
