class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0  # position to place the non-zero values
        for i in range(len(nums)): # Step 1: Move all non-zero numbers forward
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        while pos < len(nums):  # Step 2: Fill the rest with zeros
            nums[pos] = 0
            pos += 1
