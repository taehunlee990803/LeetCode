            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right 
            
        else: # current.left or current.right:
            if current.left:
                child = current.left
            else:
                child = current.right 
            if not parent:
                return child
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child 
        return root  





