                    total += 1
                return total + 1
            if ct[i][1] < k:
                k -= ct[i][1]
            elif ct[i][1] == k:
                for j in range(i+1, len(ct)):
                    total += 1
                return total
            else:
                for j in range(i+1, len(ct)):
        # temp = sorted(ct)
        for i in range(len(ct)):
        ct = sorted(ct.items(), key=lambda x:x[1])
        ct = dict(Counter(arr))

        return total
[
