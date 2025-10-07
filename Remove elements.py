class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()  #noneed but make the values in ascending order
        k=0
        n=len(nums)  #assigning length of nums to 'n'
        for i in range(n):
            if nums[i]!=val:  #condition to check value of nums is given val
                nums[k]=nums[i] #if not assign nums values to k 
                k+=1            #increment the count of size
        return k


        
        