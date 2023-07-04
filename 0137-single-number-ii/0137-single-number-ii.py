class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # counter = Counter(nums)
        # return next(element for element, count in counter.items() if count == 1)
        
        
        nums[:] = sorted(nums)

        
        n = len(nums)
        if n == 1 : return nums[0]
        if nums[0] != nums[1] : return nums[0]
        elif nums[n-1] != nums[n-2] : return nums[n-1]
        
        for i in range(1,n,3) :
            if nums[i-1] != nums[i] :
                return nums[i-1]
        return 0