class Solution:
    def singleNumber(self, nums):
        index = 0
        for num in nums:
            index ^= num  # EOR(^) helps to find unique numer in a list 
        return index