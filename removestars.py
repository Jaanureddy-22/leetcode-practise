class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        #res = [None] * (len(s) - s.count("*"))
        res=[]
        for i in s:
            if i == '*':
                res.pop()
                continue
            res.append(i)
            
        return ''.join(res)

        