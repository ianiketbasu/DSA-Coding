class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calCost(targetVal) :
            totalCost = 0
            for i in range(0,len(nums)):
                totalCost += abs(targetVal-nums[i])*cost[i]
            return totalCost
        
        low , high= min(nums) , max(nums)
        mid = (low + high) // 2
        
        while low < high :
            if calCost(mid) < calCost(mid+1) :
                high = mid
            else :
                low = mid + 1
                
            mid = (low + high) // 2
        
        return calCost(low)