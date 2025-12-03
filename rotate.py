class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #matrix[:]= list(map(list,zip(*matrix[::-1])))
        matrix.reverse()
        matrix[:]= list(map(list,zip(*matrix)))

        return matrix
        