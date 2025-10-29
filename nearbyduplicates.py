class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        dic={}
        for i in range(n):
                if nums[i] in dic and abs(i-dic[nums[i]]) <= k:
                    return True
                dic[nums[i]]=i
        return False
        