class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def convert_func(t):
            new_arr = []
        
            for element in t:
                if element == '*':
                    new_arr.pop()
                else:
                    new_arr.append(element)  
            return "".join(new_arr)
        
        return convert_func(s)
    