class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        for i in range(len(s)):
            if s[i] == ']':
                while stack[-1] != '[':
                substr = ""
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
        return ans 
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        ans = ""
            else:
                stack.append(s[i])
        while stack:
            ans = stack.pop() + ans 

