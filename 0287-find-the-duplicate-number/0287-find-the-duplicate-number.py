class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         my_set = set()
        
#         for num in nums :
#             if num in my_set:
#                 return num
#             else :
#                 my_set.add(num)
            
    
           # for mutable array
           for i in range(0,len(nums)) :
                if nums[abs(nums[i])] < 0 :
                    return abs(nums[i])
                else :
                    nums[abs(nums[i])] = -nums[abs(nums[i])]
            
