                # Traverse left subtree
                if node.left:
                    traverse(node.left, result)
                # Traverse right subtree
                if node.right:
                    traverse(node.right, result)

        # Get leaf values for both trees
        leaf_values1 = get_leaf_values(root1)
        leaf_values2 = get_leaf_values(root2)

        # Check if the leaf values are the same
        return leaf_values1 == leaf_values2

        
[3,5,1,6,2,9,8,null,null,7,4]
