class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1 : return
        
        peak_index , i = -1 , 1
        
        while i < n :
            if nums[i-1] < nums[i] :
                peak_index = i
            i += 1
        
        if peak_index == -1 :
            nums.reverse()
            return
        
        swap_index = peak_index
        for i in range(peak_index , n) :
            if nums[i] > nums[peak_index - 1] and nums[i] < nums[peak_index] :
                swap_index = i
        
        nums[peak_index - 1] , nums[swap_index] = nums[swap_index] , nums[peak_index-1]
        nums[peak_index:] = sorted(nums[peak_index : ])         
        return

        
