class Solution:
    def scoreOfString(self, s: str) -> int:
        new_arr = []
        for element in s:
            new_arr.append(ord(element))
        sum = 0

        for i in range(1,len(new_arr)):
            sum += abs(new_arr[i-1]-new_arr[i])
            print(sum)
        return sum
"
