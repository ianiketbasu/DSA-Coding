class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        total = 0
        for key,val in counter.items() :
            if val == 1 :
                total += key
        
        return total