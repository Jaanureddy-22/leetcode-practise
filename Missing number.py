class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(0 , n+1):
            if i not in nums:    #checks that any number is missing in b/w 0 to nums
                return i        #returns that missing number
        