class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
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
        """
        
        
        
        """
        row , col = len(matrix) , len(matrix[0])
        
        list1 , list2 = [1]*row, [1]*col
        
        
        for i in range(0,row*col) :
            r , c = int(i/col) , int(i%col)

            if matrix[r][c] == 0 :
                list1[r] , list2[c] = 0 , 0
        
        
        
        for i in range(0,row*col) :
            r , c = int(i/col) , int(i%col)
            
            if list1[r] == 0 or list2[c] == 0 :
                matrix[r][c] = 0
        
        """
        
        

        
       
        row, col = len(matrix), len(matrix[0])
        col_zero = False

        for i in range(row):
            if matrix[i][0] == 0:
                col_zero = True
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] , matrix[0][j] = 0 , 0

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, 0, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
            if col_zero:
                matrix[i][0] = 0
        
        
        
        
        