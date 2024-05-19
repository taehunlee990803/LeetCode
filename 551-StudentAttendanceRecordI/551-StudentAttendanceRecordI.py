        absCount = 0
        lateCount = 0
        for element in s:
            if element == 'A':
                absCount += 1


            if absCount >= 2:
                return False


                lateCount = 0
            elif element == 'L':
                lateCount += 1
            if lateCount >= 3:
                return False
        return True
            else:
                lateCount = 0
            
"
