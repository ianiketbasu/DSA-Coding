class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#         i, j = 0, 1
        
#         while j < len(nums):
#             if nums[i] != nums[j] :
#                 i += 1
#                 nums[i] = nums[j]
#             j += 1
#         i += 1
#         return i


        i = int(bool(nums))
        
        for num in nums :
            if num > nums[i-1] :
                nums[i] = num
                i += 1
        return i