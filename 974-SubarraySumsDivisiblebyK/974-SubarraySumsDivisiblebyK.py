        return count 
            else:
                prefix_map[mod] = 1
        # print(prefix_map)
                count += prefix_map[mod]
                prefix_map[mod] += 1
            if mod in prefix_map:
            # print(prefix_sum, mod)
            # if mod < 0:
            #     mod +=k
            prefix_sum += num
            mod = prefix_sum % k 
        count = 0 
        prefix_sum = 0
        prefix_map = {0:1}
        for num in nums:
        # count = 0

[
