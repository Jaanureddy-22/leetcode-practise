class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        longest=""
        for i in range(n):   #to check all chars in str
            for j in range(i,n):  
                substr=s[i:j+1]  #substring
                if(substr==substr[::-1] and len(substr)>len(longest)):  #checks is it palindrome or not
                    longest=substr    #assigning substr to a variable
        return longest   
