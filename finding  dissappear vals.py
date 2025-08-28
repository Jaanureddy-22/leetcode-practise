class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        s=set(nums)   #reduces time complexity by using sets
        for i in range(1,len(nums)+1):  #checks the elements upto given range 
            if i not in s:             #condition to check if i not present in given nums
                res.append(i)    #displays the value which is  not present in nums
        return res
        