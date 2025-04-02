                child = current.right
            if not parent:
                return child
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child

        else: # Node has left and right children
            # Need to find the smallest node in the right subtree
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            current.val = successor.val

            if successor_parent.left == successor:
                successor_parent.left = successor.right

            else:
                successor_parent.right = successor.right
        return root 

