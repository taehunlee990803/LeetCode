# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        queue = deque([root])
        # min_ans = float('inf')

        while queue:
            node = queue.popleft()
            # current = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                # min_ans = min(min_ans, abs(node.left.val - current))
                # min_ans = min(min_ans, abs(node.right.val - current))
        return min_ans

        val_container = []
            val_container.append(node.val)
        val_container.sort()
        for i in range(1, len(val_container)):
            min_ans = min(min_ans,val_container[i]-val_container[i-1])
        min_ans = float('inf')

