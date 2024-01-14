class Solution:
    def minSteps(self, s: str, t: str) -> int:
        memo = collections.defaultdict(int)
        for char in s:
            memo[char] += 1
        for char in t:
            if memo[char]:
                memo[char] -=1 
        return sum(memo.values())
"bab"
