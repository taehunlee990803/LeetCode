                container.append([arr[i], arr[j]])
                fraction[ans] = count
                ans = arr[i]/arr[j]
                count += 1
        

        fraction = dict(sorted(fraction.items()))
        for i, element in enumerate(fraction):
            if i == k -1:
        loc = 0
                loc = fraction[element]

                return container[loc]



        return []
[
