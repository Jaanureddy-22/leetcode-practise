class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev=s[::-1]
        for i in range(len(s)):
            if s.startswith(rev[i:]): #checks that given str is a planidrome or not
                return rev[:i]+s      # add characters infront of shortest prefix to make it palindrome

        return ""
        