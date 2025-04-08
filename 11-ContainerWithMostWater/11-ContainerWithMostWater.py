
            if left < right:

            currentArea = (r-l)*currentHeight
            maxAmount = max(maxAmount, currentArea)
            left = height[l]
            right = height[r]
            currentHeight = min(left, right)
                l += 1
            else:

                r -= 1
        return maxAmount










