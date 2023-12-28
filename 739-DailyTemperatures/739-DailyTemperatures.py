class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] * len(temperatures)
        count = 0
        length = len(temperatures)
        for i in range(0,length):
            current = temperatures[i]
            for j in range(i+1, length):
                if temperatures[j] > current:
                    break
            # count = 0
        return stack
        
                    stack[i] = j - i
        # result = [0]*len(temperatures)
        # stack = []
        # for index, temp in enumerate(temperatures):
        #         prev_temp = stack.pop()
        #     while stack and temperatures[stack[-1]] < temp:
        #         result[prev_temp] = index - prev_temp
        #     stack.append(index)
        # return result



[
