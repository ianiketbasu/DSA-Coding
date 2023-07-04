class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        
        
        return next(element for element, count in counter.items() if count == 1)