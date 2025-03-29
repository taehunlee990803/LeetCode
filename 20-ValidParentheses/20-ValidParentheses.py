        #     last = stack.pop()
        #     first = s[idx]
        
        # while len(stack) // 2 > 0:
        #     stack.append(element)

        # idx = 0
        if len(stack) == 0:
        # for element in s:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')' : '(',']' : '[', '}' : '{'}
        for element in s:
            if stack and (element in hashmap and stack[-1] == hashmap[element]):
                stack.pop()
            else:
                stack.append(element)
            return True
        else:
            return False
