class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        # Slide the window across the array
        for i in range(k, len(nums)):
            max_sum = max(max_sum, current_sum)  # Update max sum if needed
        
            current_sum += nums[i] - nums[i - k]  # Add new element, remove old element
        max_sum = current_sum  # Set max sum initially to the first k-element sum

        return max_sum / k  # Return max average

