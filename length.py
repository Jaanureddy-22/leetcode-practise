class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # using inbuilt methods
        s.strip()
        words=s.split()
        return len(words[-1])
    


        # without inbuilt methods
        length = 0
        i = len(s) - 1

        # Step 1: Skip whitespaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Step 2: Count letters of last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


        