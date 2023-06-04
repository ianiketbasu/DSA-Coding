class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(0,n*m) :
            if matrix[int(i/m)][int(i%m)] == target :
                return True
        
        return False
        