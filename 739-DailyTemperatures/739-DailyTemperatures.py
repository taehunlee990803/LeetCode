class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List
[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_temp = stack.pop()
                result[prev_temp] = index - prev_temp
            stack.append(index)
        return result
