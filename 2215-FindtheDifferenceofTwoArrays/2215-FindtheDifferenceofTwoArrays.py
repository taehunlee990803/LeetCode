class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1 = []
        answer2 = []

        for element in nums1:
            if element not in nums2 and element not in answer1:
                answer1.append(element)
        for element in nums2:
            if element not in nums1 and element not in answer2:
                answer2.append(element)
        ans = []
        ans = [answer1, answer2]

        return ans 

