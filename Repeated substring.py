class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
          
        if s in (s+s)[1:-1]:
            return True
        return False
        