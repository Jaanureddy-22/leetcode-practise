class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        s=[]
        for op in operations:
            if op == 'C':
                s.pop()
            elif op == 'D':
                s.append(int(2*s[-1]))
            elif op == '+':
                s.append(int(s[-1])+int(s[-2]))
            else:
                s.append(int(op))
                
        return sum(s)

        