        # if len(nums) % 2 == 0:
        # else:
        #     mid = (len(nums) + 1)// 2
        #     mid = len(nums) // 2

        # root = TreeNode(nums[mid])
        # left = nums[:mid]
        # right = nums[mid:]

        # for i in range(len(left)-1,-1,-1):
        # first = True

        #     if first:
        #     temp_node = TreeNode(left[i])
        root = TreeNode(nums[mid])


        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
        mid = len(nums) // 2

            return None
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
#         self.left = left
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
