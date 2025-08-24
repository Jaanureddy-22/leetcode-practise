class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            while num >= 10:  # to check num is single digit or not
                sum_of_digits=0
                while num != 0:  #to check that  number !=0
                    digit=num%10   #gives the last digit in num
                    sum_of_digits += digit
                    num //= 10    #updated num
                num=sum_of_digits  #assgining sum of digits to num
            return num
    
         
        