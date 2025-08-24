class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:]=list(dict.fromkeys(nums)) # dictonary helps not to allow duplicates
        nums.sort()
        return len(nums)
    
        