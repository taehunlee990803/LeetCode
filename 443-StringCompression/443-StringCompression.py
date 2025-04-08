        s = ""
        if len(chars) == 1:
            s+=chars[0]
            # chars = s
            return 1
        else:
            s+=chars[0]
            i = 0
            while i < len(chars):
                count = 1
                while (i + count) < len(chars) and chars[i + count] == chars[i]:
                    # i += 1
                    count += 1
            insert = 0
                chars[insert] = chars[i]
                i += count 
                insert += 1
                if count > 1:
                    string = str(count)
                    chars[insert:insert + len(string)] = list(string)
                    insert += len(string)
    def compress(self, chars: List[str]) -> int:
class Solution:
