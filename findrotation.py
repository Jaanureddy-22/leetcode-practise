class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for i in range(4):
            if mat == target:
                return True
            mat[:]=list(map(list,zip(*mat[::-1])))
                
        return False
        
        