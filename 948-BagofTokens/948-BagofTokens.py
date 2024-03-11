        return res
                score -= 1
                r -= 1
                power += tokens[r]
            elif score >= 1:
                res = max(res,score)
                l += 1
                score += 1
                power -= tokens[l]
            if power >= tokens[l]:
        while l <= r:
        res = 0
        l,r = 0, len(tokens)-1
        currentPower = power
        # print(tokens)
        tokens.sort()
        score = 0
            else:
                break
[
