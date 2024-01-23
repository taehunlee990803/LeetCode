class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        maxlen = 0
        unique = ['']

        
        for word in arr:
            for j in unique:
                temp = j + word 
                if len(temp) == len(set(temp)):
                    unique.append(temp)
                    maxlen = max(maxlen, len(temp))
        return maxlen
  
[
