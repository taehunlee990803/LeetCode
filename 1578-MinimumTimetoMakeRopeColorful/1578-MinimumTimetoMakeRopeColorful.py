                temp = neededTime[element]
            if neededTime[element] <= neededTime[element+1]:
        for element in container:
        print(container)
                neededTime[element] = neededTime[element+1]
                
            else:
                temp = neededTime[element+1]
                neededTime[element+1] = neededTime[element]
            # temp = min(neededTime[element], neededTime[element+1])
            minimum += temp
            print(temp)
            # print(minimum)
        return minimum


"
