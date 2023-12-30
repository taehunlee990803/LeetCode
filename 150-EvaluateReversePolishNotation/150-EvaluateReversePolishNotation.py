        return int(num_stack[0])

        # if len(num_stack) == 1:
                num_stack.append(element)
            
            else:
                num_stack.append(ans)
        
                    ans = temp1 * temp2
                else:
                    ans = int(temp1/temp2)
                elif element == '-':
                    ans = temp1 - temp2
                elif element == '*':
        operator_stack = []
        operator = ['+', '-','*','/']
        for element in tokens:
            if element in operator:
                temp2 = int(num_stack.pop())
                temp1 = int(num_stack.pop())
                if element == '+':
                    ans = temp1 + temp2
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
               ·····#·if·ans·<·0:
····················#·····ans·=·0

        # while operator_stack:
[
