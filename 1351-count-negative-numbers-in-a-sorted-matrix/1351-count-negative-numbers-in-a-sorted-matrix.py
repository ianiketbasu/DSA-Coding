class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def biSearch(grid: List[List[int]]) -> int:
            low , high = 0 , len(grid) - 1
            
            while low <= high :
                mid = (low + high) // 2
                if grid[mid] >= 0 : low = mid + 1
                else : high = mid - 1
            
            return len(grid)  - low
        
        count = 0
        
        for row in grid :
            count += biSearch(row)
        
        return count