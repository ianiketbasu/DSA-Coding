class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low , high = 1 , max(nums)
        
        while low < high :
            mid = (low + high) // 2
            t_val = sum(ceil(eli/mid) for eli in nums)
            if t_val > threshold :
                low = mid + 1
            else :
                high = mid
                
        return low