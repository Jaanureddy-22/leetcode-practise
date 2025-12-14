class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
     
        val=int(str(abs(num))[::-1])*(-1 if num <0 else 1)
        if num == int(str(abs(val))[::-1]*(-1 if val < 0 else 1)):
            return True
        return False
        
        