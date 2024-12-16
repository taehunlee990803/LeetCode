class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List
[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize the result array with all 

        # Iterate through each day
        for i in range(n):
            # Check all future days
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
zeros
                    result[i] = j - i  # Store the difference in 
days
                    break  # Exit the loop once we find a warmer day

        return result
