#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        arr.sort()
        n=len(arr)
        for i in range(n):
            if i == k-1:
                return arr[i]
        
        
