            if i == 0:
                ranks[score_positions[sorted_scores[i]]] = "Gold Medal"
            elif i == 1:
                ranks[score_positions[sorted_scores[i]]] = "Silver Medal"
            elif i == 2:
                ranks[score_positions[sorted_scores[i]]] = "Bronze Medal"
            else:
                ranks[score_positions[sorted_scores[i]]] = str(i + 1)
        
        # Create the final result list based on the original order of scores
        result = [ranks[i] for i in range(len(score))]
        
        return result

        
[
