
        for i in range(k, len(s)):
            if s[i] in vowels:  # Add new character
                count += 1
            if s[i - k] in vowels:  # Remove old character
                count -= 1
            max_value = max(max_value, count)
        
        return max_value

        max_value = count
                count += 1
        vowels = ['a', 'e','i','o','u']
        count = 0
        for i in range(0,k):
            if s[i] in vowels:
