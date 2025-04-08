


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        ans = []

        for num in nums1_set:
        temp = []
        temp = []
            if num not in nums2_set:
                temp.append(num)
        ans.append(temp)
        for num in nums2_set:
            if num not in nums1_set:
                temp.append(num)
        return ans
        ans.append(temp)



