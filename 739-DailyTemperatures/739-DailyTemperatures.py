
        result = [0]*len(temperatures)
       
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
class Solution:
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_temp = stack.pop()
          ······result[prev_temp]·=·index·-·prev_temp
············stack.append(index)
········return·result

[73,74,75,71,69,72,76,73]
