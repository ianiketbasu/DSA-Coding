class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
#         for i in range(0,n*m) :
#             if matrix[int(i/m)][int(i%m)] == target :
#                 return True
        
#         return False

        low , high = 0 , m*n - 1
        
        while low <= high :
            mid = (low + high) // 2
            if matrix[int(mid/m)][int(mid%m)] == target :
                return True
            elif matrix[int(mid/m)][int(mid%m)] < target :
                low = mid + 1
            else :  high = mid - 1
        
        return False
        