class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pair = defaultdict(int)
#         operation = 0
#         duplicate = nums
        
#         nums_freq = dict(Counter(nums))
        
        count_pairs = 0
        
        for num in nums:
            if pair[num]:
                count_pairs+=1
                pair[num] -=1
            else:
                pair[k-num] +=1
        return count_pairs
#         for num in nums:
#             if nums_freq[num] > 0:
#                 complement = k - num
                
#                 if complement == num:
#                     if complement in nums_freq and nums_freq[complement] > 1:
#                         count_pairs += 1
#                         nums_freq[num] -= 1
#                         nums_freq[complement] -= 1
#                         print(num,nums_freq)
#                 else:
#                     if complement in nums_freq and nums_freq[complement] > 0:
#                         count_pairs += 1
#                         nums_freq[num] -= 1
#                         nums_freq[complement] -= 1
#                         print(num,nums_freq)
                    
#         return count_pairs
    
    