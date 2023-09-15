class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        find = True
        
        for i in range(0,len(nums1)):
            find = True
            for j in range(0,len(nums2)):
                if nums2[j] == nums1[i]:
                    for k in range(j,len(nums2)):
                        if nums2[k] > nums2[j]:
                            result.append(nums2[k])
                            find = False
                            break
                    if find is True:
                        result.append(-1)
                    
        return result