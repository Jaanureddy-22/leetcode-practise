class Solution(object):
    @staticmethod #helps to work without self function
    def myfunc(x):
        if len(x) == 0:
            return False
        else:
            y = x[::-1]
            return x == y  # returns True if palindrome, False otherwise

# Input
z = input("Enter your value: ")
result = Solution.myfunc(z)
print(result)
