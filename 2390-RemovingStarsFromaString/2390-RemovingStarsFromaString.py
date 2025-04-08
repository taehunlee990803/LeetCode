













            else:
                stack.pop()

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for element in s:
            if element != '*':
                stack.append(element)
        return ''.join(stack)
