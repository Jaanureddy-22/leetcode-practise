class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
     
        if num%10 != 0  or num == 0:
            return True
        return False
        
        