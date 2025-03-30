class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # exp = []
        # num = []
        # ans = 1
        # valid_op = ['+', '-', '/', '*']

        stack = []
        for t in tokens:
            if t not in valid_op:
        valid_op = ['+', '-', '/', '*']
                stack.append(int(t))
            else:
                r,l = stack.pop(), stack.pop()
                if t == '+':
                elif t == '-':
                elif t == '*':
                elif t == '/':
                    stack.append(l+r)
                    stack.append(l-r)
                    stack.append(l*r)
                    stack.append(int(float(l)/r))
        return stack.pop()
