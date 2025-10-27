class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        n = x/2.0
        while abs(n * n - x) > 0.00001:   # tolerance level
              n = (n + x / n) / 2
        
        return int(n)  if(int(n)*int(n) <= x) else int(n)-1 