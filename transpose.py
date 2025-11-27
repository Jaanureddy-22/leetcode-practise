class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        result=list(map(list,zip(*matrix))) #zip() pairs elements from multiple sequences index-wise.
        return result
        