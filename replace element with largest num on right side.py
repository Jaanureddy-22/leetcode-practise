class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr)==0:  #if length=0 it returns nothing
            return ""
        elif len(arr)==1:  #if length=1 it returns -1
            return [-1]
        else:
            n=len(arr)
            max_value=-1  #last value should replace with -1
            for i in range(n-1,-1,-1): #loop to check from last
                curr=arr[i]
                arr[i]=max_value
                if curr>max_value:
                    max_value=curr
            return arr



        