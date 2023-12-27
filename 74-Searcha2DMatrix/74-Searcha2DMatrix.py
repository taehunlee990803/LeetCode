                    m = (l+r)//2
                    if element[m] == target:
                        return True
                    elif element[m] > target:
                        r = m - 1
                    else:
                        l = m + 1

           

        return False
                while l<=r:
[
