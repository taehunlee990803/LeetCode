class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        arr = [0,1,1]
        i = 0
        
        while i<=n:
            arr.append(arr[i]+arr[i+1]+arr[i+2])
            i+=1
        return arr[n]
        
        