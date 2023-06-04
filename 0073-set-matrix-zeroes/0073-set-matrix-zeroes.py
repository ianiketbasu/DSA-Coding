class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row , col = len(matrix) , len(matrix[0])
        coordinates = []
        def makeZero(coordinate) :
            a , b = coordinate
            for i in range(a,-1,-1) :
                matrix[i][b] = 0
            for i in range(a,row) :
                matrix[i][b] = 0
                
            for j in range(b,-1,-1) :
                matrix[a][j] = 0
            for j in range(b,col) :
                matrix[a][j] = 0
                
                
        for i in range(0,row*col) :
            r , c = int(i/col) , int(i%col)

            if matrix[r][c] == 0 :
                coordinates.append((r,c))
            
        for coordinate in coordinates :
            makeZero(coordinate)