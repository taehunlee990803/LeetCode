class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for element in stones:
            for jewel in jewels:
                if element == jewel:
                    count += 1
        return count 
"
