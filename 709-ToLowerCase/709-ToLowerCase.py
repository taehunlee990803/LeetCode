class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = 0
        lower = 0

        for element in word:
            if ord(element) >= 65 and ord(element) <= 90:
                capital += 1
            else:
                lower += 1

        if lower == 0 and capital != 0:
            return True
        if lower != 0 and capital == 0:
            return True

        if capital == 1 and (ord(word[0]) >= 65 and ord(word[0]) <= 90):
            return True
        print(lower, capital)
        return False
"
