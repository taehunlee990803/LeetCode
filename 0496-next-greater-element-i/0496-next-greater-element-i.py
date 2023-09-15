class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        find = True
        nums1_length = len(nums1)
        nums2_length = len(nums2)
         
        # for i in range(0,len(nums1)):
        #     find = True
        #     for j in range(0,len(nums2)):
        #         if nums2[j] == nums1[i]:
        #             for k in range(j,len(nums2)):
        #                 if nums2[k] > nums2[j]:
        #                     result.append(nums2[k])
        #                     find = False
        #                     break
        #             if find is True:
        #                 result.append(-1)
        temp_index = 0
        for i in range(0,nums1_length):
            find = True
            temp_index = nums2.index(nums1[i])
            
            for j in range(temp_index, nums2_length):
                if nums2[j] > nums1[i]:
                    result.append(nums2[j])
                    find = False
                    break
            if find is True:
                result.append(-1)
                    
            
#             for j in range(0,len(nums2)):
#                 if nums2[j] == nums1[i]:
#                     for k in range(j,len(nums2)):
#                         if nums2[k] > nums2[j]:
#                             result.append(nums2[k])
#                             find = False
#                             break
#                     if find is True:
#                         result.append(-1)
                    
        return result