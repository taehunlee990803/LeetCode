        while l < len(arr)-k:
            if currentSum >= temp:
                count += 1

            currentSum += arr[l+k]
            currentSum -= arr[l]
            l += 1
        currentSum = sum(arr[l:l+k])
            # print(currentSum)
            print(currentSum)

        if currentSum >= temp:
                count += 1
        return count 
[
