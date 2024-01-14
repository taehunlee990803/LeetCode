            rank_dict[s] = "Bronze Medal"
        elif i == 2:
            rank_dict[s] = "Silver Medal"
        else:
            rank_dict[s] = str(i + 1)
    
    # Create a list to store the results
    result = []
    
    # Loop through the input array and append the rank of each score to the result list
    for s in score:
        result.append(rank_dict[s])
    
    # Return the result list
    return result
[
