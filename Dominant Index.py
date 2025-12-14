class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val=max(nums) #max val in given list
        for i in range(len(nums)):
            if  i != nums.index(val) and val < 2*nums[i]: #skip the max value and compare with others
               return -1
        return nums.index(val) # if condition not satisfy return indexof max val
        
            
        