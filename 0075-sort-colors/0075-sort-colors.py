class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums[:] = sorted(nums)
        
        zero_cnt , one_cnt , two_cnt = 0 ,0,0
        
        for num in nums :
            if num == 0 :
                zero_cnt += 1
            elif num == 1 :
                one_cnt += 1
            else : two_cnt += 1
        
        for i in range(0,len(nums)) :
            if zero_cnt > 0 :
                nums[i] = 0
                zero_cnt -= 1
            elif one_cnt > 0 :
                nums[i] = 1
                one_cnt -= 1
            elif two_cnt > 0 :
                nums[i] = 2
                two_cnt -= 1