class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_val = int(str(abs(x))[::-1])*(-1 if x < 0 else 1)
        return reverse_val if pow(-2,31) <= reverse_val < pow(2,31) else 0