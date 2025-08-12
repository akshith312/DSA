class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        ROWS,COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS+1) for r in range(ROWS+1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix+= matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix + above        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        #brute force
        # sum = 0

        # for i in range(row1, row2+1):
        #     for j in range(col1, col2+1):
        #         sum+= self.matrix[i][j]
        # return sum

        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1-1][col2]
        left = self.sumMat[row2][col1-1]
        topLeft = self.sumMat[row1-1][col1-1]

        return bottomRight - above - left + topLeft






        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)