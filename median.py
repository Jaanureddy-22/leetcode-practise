from decimal import Decimal
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        if(n%2 == 0):  #if length of n is even 
             mid1 = Decimal(nums1[n//2])   
             mid2 = Decimal(nums1[n//2-1])
             median = (mid1+mid2)/Decimal(2)
        else:                                  #if length is odd
             median = Decimal(nums1[n//2])
        return median