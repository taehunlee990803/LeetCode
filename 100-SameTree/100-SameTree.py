            for i in range(len(q1)):
            if len(q1) != len(q2):
                return False
        while q1 and q2:
        q2 = deque([q])

        q1 = deque([p])
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
class Solution:
#         self.left = left
#         self.right = right
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
# class TreeNode:
# Definition for a binary tree node.

        if not p and not q:
            return True
        if not p and q:
            return False
        if not q and p:
            return False
