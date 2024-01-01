class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = Counter(s)
        temp = [key for key, value in dic.items() if value >= 2]
        if not temp:
            return -1  # No repeated characters found

        max_length = 0
        for char in temp:
            first_occurrence = s.index(char)
            last_occurrence = s.rindex(char)
            length = last_occurrence - first_occurrence - 1
            max_length = max(max_length, length)

        return max_length
"
