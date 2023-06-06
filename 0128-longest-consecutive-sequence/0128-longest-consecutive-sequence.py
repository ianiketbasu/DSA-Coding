class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        nums[:] = sorted(nums)
        prev_num , max_len , count = float('-inf') , 1 , 0

        
        for num in nums :
            if num - 1 == prev_num :
                count += 1
                prev_num = num
                
            elif num != prev_num :
                count = 1
                prev_num = num
            
            max_len = max(max_len , count)
            
        return max_len