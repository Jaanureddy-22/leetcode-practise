class Solution(object):
    def isPalindrome(self, s):
        chk = [ch.lower() for ch in s if ch.isalnum()]  # logic for not to allow non aplhanumeric  characters
        return chk == chk[::-1]  # if condtition satisfies returns true or else false