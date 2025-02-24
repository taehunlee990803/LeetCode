class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        # answer2 = []
        # ans = []

        # for element in nums1:
        #     if element not in nums2 and element not in answer1:
        #         answer1.append(element)
        # for element in nums2:
        #     if element not in nums1 and element not in answer2:
        #         answer2.append(element)
        # ans = [answer1, answer2]

        # return ans 
        # answer1 = []
        return [list(set1 - set2), list(set2 - set1)]
        

