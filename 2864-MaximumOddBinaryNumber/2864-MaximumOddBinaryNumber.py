class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = Counter(s)
        numOne = s['1']
        numZero = s['0']

        ans = ""
        if numOne >= 2:
            while numOne > 1:
                ans += "1"
        else:
            ans += "0" * numZero
            ans += "1"
            return ans 
        print(numOne, numZero)
                numOne -= 1
            return ans 
            ans += "1"
            ans += "0" * numZero
            print("Y")


"
