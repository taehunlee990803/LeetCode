class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
#         def int_to_array(number):
#             if number == 0:
#                 return [0]
            
#             num_str = str(abs(number))
#             digit_list = [int(digit) for digit in num_str]
            
#             return digit_list if number >=0 else [-digit for digit in digit_list]
        
#         new_list = int_to_array(n)
#         new_list = new_list.sort(reverse = True)
        
#         count = 0
        
#         for i in range(0,len(new_list)):
#             if n[i] == '1':
#                 count+=1
#             else:
#                 return count