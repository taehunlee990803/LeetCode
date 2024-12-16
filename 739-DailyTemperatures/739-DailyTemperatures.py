class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        n = len(temperatures)
        for i in range(n):
            current = temperatures[i]
            count = 1
            for j in range(i+1, n):
                if temperatures[j] > current:
                    output.append(count)
                    break
                else:
            temp = -1
                    temp = 0
                    count += 1
            if temp == -1:
                output.append(0)

        return output 
