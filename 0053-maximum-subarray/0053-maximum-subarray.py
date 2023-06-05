class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ele_sum , max_sum = 0 , float('-inf')
        
        for num in nums :
            ele_sum += num
            
            if max_sum < ele_sum :
                max_sum = ele_sum
            
            if ele_sum < 0 :
                ele_sum = 0
        
        return max_sum