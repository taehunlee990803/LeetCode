                            temp = nums[i]
                            nums[i] = nums[j]
                            nums[j] = temp
                            break

        for num in nums:
            if num == 0:
                check = False
        if check:
            return
        else:
            for i in range(0, len(nums)):
                if nums[i] == 0:
                    for j in range(i+1, len(nums)):
                        if nums[j] != 0:
        check = True
        """
        Do not return anything, modify nums in-place instead.
        """
    def moveZeroes(self, nums: List[int]) -> None:
