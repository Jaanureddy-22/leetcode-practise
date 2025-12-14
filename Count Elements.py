class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minval=min(nums)
        maxval=max(nums)
        count=0
        for i in range(len(nums)):
            if   nums[i] > minval and nums[i] < maxval:
                count+=1
        return count