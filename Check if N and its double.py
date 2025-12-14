class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        visited = set()
        for  val in arr:
            if 2*val in visited or ( val%2 ==0 and val//2 in visited):
                return True
            visited.add(val)
        return False




